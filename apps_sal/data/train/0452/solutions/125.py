import numpy as np


class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        dp = np.zeros((n, d + 1))
        if d > n:
            return -1

        def rdp(i, j):
            if dp[i, j] == 0:
                if j <= n - i:
                    if j == 1:
                        dp[i, j] = max(jobDifficulty[i:])
                    else:
                        dp[i, j] = min([max(jobDifficulty[i:k]) + rdp(k, j - 1) for k in range(i + 1, n)])
                else:
                    dp[i, j] = float('inf')
            return dp[i, j]
        return int(rdp(0, d))
