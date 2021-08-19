class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        self.memo = {}
        return self.helper(0, 0, '', s, k)

    def helper(self, i, last_count, last_ch, s, k):
        if i == len(s):
            length_count = len(str(last_count)) if last_count > 1 else 0
            length_ch = len(last_ch)
            return length_count + length_ch
        if (i, last_count, last_ch, k) in self.memo:
            return self.memo[i, last_count, last_ch, k]
        delete = float('inf')
        if k > 0:
            delete = self.helper(i + 1, last_count, last_ch, s, k - 1)
        if s[i] == last_ch:
            no_delete = self.helper(i + 1, last_count + 1, last_ch, s, k)
        else:
            length_count = len(str(last_count)) if last_count > 1 else 0
            length_ch = len(last_ch)
            no_delete = length_count + length_ch + self.helper(i + 1, 1, s[i], s, k)
        res = min(delete, no_delete)
        self.memo[i, last_count, last_ch, k] = res
        return res
