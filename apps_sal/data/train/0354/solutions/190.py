class Solution:
    def dieSimulator(self, n, rollMax):
        if n == 1:
            return 6
        mod = int(1e9 + 7)
        dp = [[[0] * 15 for j in range(6)] for i in range(n)]
        for i in range(6):
            dp[0][i][0] = 1
        for i in range(1, n):
            for p in range(6):
                for j in range(6):
                    for k in range(15):
                        if p != j:
                            dp[i][j][0] = (dp[i][j][0] + dp[i - 1][p][k]) % mod
                        elif k > 0 and k < rollMax[j]:
                            dp[i][j][k] = dp[i - 1][j][k - 1]
        ans = 0
        for j in range(6):
            for k in range(15):
                ans = (ans + dp[-1][j][k]) % mod
        return ans
