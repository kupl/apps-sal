import numpy as np


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = np.empty((n, n))
        for j in range(1, n):
            dp[j - 1, j] = abs(piles[j - 1] - piles[j])

        for j in range(3, n, 2):
            for i in range(0, n - j):
                # want to get dp[i,i+j]
                # crrespond dp[i,i+j-2] dp[i+1,i+j-1],dp[i-2,i+j]
                temp1 = piles[i + j] + min(-piles[i + j - 1] + dp[i, i + j - 2], -piles[i] + dp[i + 1, i + j - 1])
                temp2 = piles[i] + min(-piles[i + 1] + dp[i + 2, i + j], -piles[i + j] + dp[i + 1, i + j - 1])
                dp[i, i + j] = max(temp1, temp2)
        if dp[0, n - 1] > 0:
            return True
        else:
            return False
