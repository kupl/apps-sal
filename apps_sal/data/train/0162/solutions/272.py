import numpy as np


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str):
        dp = np.full((len(text1) + 1, len(text2) + 1), 0)
        print(dp.shape)
        for i in range(dp.shape[0] - 2, -1, -1):
            for j in range(dp.shape[1] - 2, -1, -1):
                if text1[i] == text2[j]:
                    dp[i, j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i, j] = max(dp[i + 1, j], dp[i, j + 1])
        return dp[0, 0]
