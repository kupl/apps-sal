class Solution:

    def removeDuplicates(self, s: str, k: int) -> str:
        res = []
        char = s[0]
        count = 1
        for i in range(1, len(s)):
            if s[i] == char:
                count += 1
            else:
                count = 1
                char = s[i]
            if count == k:
                return self.removeDuplicates(s[:i - k + 1] + s[i + 1:], k)
        return s
