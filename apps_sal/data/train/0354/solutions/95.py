class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[[0 for k in range(16)] for j in range(6)] for i in range(n)]

        for s in range(6):
            dp[0][s][1] = 1

        for i in range(1, n):
            for j in range(6):
                for k in range(1, rollMax[j] + 1):
                    if k > 1:
                        dp[i][j][k] = dp[i - 1][j][k - 1]
                    else:
                        for jj in range(6):
                            for kk in range(1, rollMax[jj] + 1):
                                if j == jj:
                                    continue
                                dp[i][j][k] += dp[i - 1][jj][kk]
        ans = 0
        for l in range(6):
            for m in range(1, rollMax[l] + 1):
                ans += dp[n - 1][l][m]

        return ans % (10**9 + 7)
