import numpy as np


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0

        m = len(text1)
        n = len(text2)

        A = np.zeros((m + 1, n + 1), int)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    A[i, j] = A[i - 1, j - 1] + 1
                else:
                    A[i, j] = max(A[i - 1, j], A[i, j - 1])
        return A[-1, -1]
