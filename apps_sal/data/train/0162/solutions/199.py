import numpy as np
from functools import lru_cache


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        m = len(text1)
        n = len(text2)
        return self.dp(text1, text2, m - 1, n - 1)

    @lru_cache(maxsize=None)
    def dp(self, text1, text2, i, j):
        if i < 0 or j < 0:
            return 0
        if text1[i] == text2[j]:
            return self.dp(text1, text2, i - 1, j - 1) + 1
        else:
            return max(self.dp(text1, text2, i - 1, j), self.dp(text1, text2, i, j - 1))
