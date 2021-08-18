class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[[0 for k in range(16)] for j in range(7)] for i in range(n + 1)]
        mod = pow(10, 9) + 7

        for j in range(1, 7):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(1, 7):
                for k in range(1, 16):
                    if k != 1:
                        if k <= rollMax[j - 1]:
                            dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][k - 1]) % mod
                    else:
                        for jj in range(1, 7):
                            if jj != j:
                                for kk in range(16):
                                    dp[i][j][k] = (dp[i][j][k] + dp[i - 1][jj][kk]) % mod

        ans = 0
        for j in range(1, 7):
            for k in range(1, 16):
                ans = (ans + dp[n][j][k]) % mod

        return ans
