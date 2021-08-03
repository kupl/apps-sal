class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0 for _ in range(7)] for _ in range(n + 1)]
        dp[0][6] = 1
        for j in range(6):
            dp[1][j] = 1
        dp[1][6] = sum(dp[1])
        for i in range(2, n + 1):
            for j in range(6):
                dp[i][j] = dp[i - 1][6]
                if i - rollMax[j] - 1 >= 0:
                    dp[i][j] -= dp[i - rollMax[j] - 1][-1] - dp[i - rollMax[j] - 1][j]
            dp[i][-1] = sum(dp[i])
        return dp[n][6] % 1000000007
