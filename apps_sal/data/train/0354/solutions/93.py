class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[[0 for k in range(16)] for j in range(7)] for i in range(n + 1)]
        mod = pow(10, 9) + 7
        for j in range(1, 7):
            dp[1][j][1] = 1
        for i in range(2, n + 1):
            for j in range(1, 7):
                for prev in range(1, 7):
                    for k in range(1, rollMax[prev - 1] + 1):
                        if j != prev:
                            dp[i][j][1] = (dp[i][j][1] + dp[i - 1][prev][k]) % mod
                        elif k < rollMax[prev - 1]:
                            dp[i][j][k + 1] = dp[i][j][k + 1] + dp[i - 1][j][k]
        ans = 0
        for j in range(1, 7):
            for k in range(1, rollMax[j - 1] + 1):
                ans = (ans + dp[n][j][k]) % mod
        return ans
