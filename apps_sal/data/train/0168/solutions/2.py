class Solution:

    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        if n == k:
            return True
        ch_to_cnt = collections.defaultdict(int)
        for ch in s:
            ch_to_cnt[ch] += 1
        for cnt in ch_to_cnt.values():
            if cnt % 2 == 1:
                k -= 1
        return k >= 0
