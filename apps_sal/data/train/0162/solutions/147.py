from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1, t2 = text1, text2

        @lru_cache(None)
        def lcsh(m, n):
            nonlocal t1, t2
            if m == 0 or n == 0:
                return 0
            if t1[m - 1] == t2[n - 1]:
                return 1 + lcsh(m - 1, n - 1)
            else:
                return max(lcsh(m - 1, n), lcsh(m, n - 1))
        return lcsh(len(text1), len(text2))
