from functools import lru_cache


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(None)
        def dp(i, j, strx, stry):
            if i >= len(strx) or j >= len(stry):
                return 0
            elif strx[i] == stry[j]:
                return 1 + dp(i + 1, j + 1, strx, stry)
            else:
                return max(dp(i, j + 1, strx, stry), dp(i + 1, j, strx, stry))
        return dp(0, 0, text1, text2)
