class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        m = len(rollMax)
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
        dp[0][m] = 1
        for j in range(m):
            dp[1][j] = 1
        dp[1][m] = m
        for i in range(2, n + 1):
            for j in range(m):
                for k in range(1, rollMax[j] + 1):
                    if i - k < 0:
                        break
                    dp[i][j] += dp[i - k][m] - dp[i - k][j]
            dp[i][m] = sum(dp[i])
        return dp[n][m] % (10**9 + 7)
