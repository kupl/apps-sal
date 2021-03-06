class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        M = pow(10, 9) + 7
        rollMax = [0] + rollMax
        dp = [[[0] * (15 + 1) for _ in range(6 + 1)] for _ in range(n + 1)]
        for i in range(1, 6 + 1):
            dp[1][i][1] = 1
        for i in range(2, n + 1):
            for j in range(1, 6 + 1):
                for k in range(1, rollMax[j] + 1):
                    if k > 1:
                        dp[i][j][k] = dp[i - 1][j][k - 1]
                    else:
                        for jj in range(1, 6 + 1):
                            for kk in range(1, rollMax[jj] + 1):
                                if jj != j:
                                    dp[i][j][k] += dp[i - 1][jj][kk]
        res = 0
        for i in range(1, 7):
            for j in range(1, rollMax[i] + 1):
                res += dp[n][i][j]
        return res % M
