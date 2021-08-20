from functools import lru_cache


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def memo(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + max(memo(i + 1, j + 1), memo(i + 1, j + 1))
            else:
                return max(memo(i + 1, j), memo(i, j + 1))
        return memo(0, 0)
