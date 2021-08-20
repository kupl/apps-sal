class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        from functools import lru_cache
        memo = {}

        @lru_cache(maxsize=None)
        def lcs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[i, j]
            elif text1[i] == text2[j]:
                r = 1 + lcs(i + 1, j + 1)
            else:
                r = max(lcs(i + 1, j), lcs(i, j + 1))
            memo[i, j] = r
            return r
        return lcs(0, 0)
