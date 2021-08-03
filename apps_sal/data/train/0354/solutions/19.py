class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0 for i in range(7)] for j in range(n + 1)]
        dp[0][6] = 1
        for j in range(6):
            dp[1][j] = 1
        dp[1][6] = 6

        for i in range(2, n + 1):
            for j in range(6):
                for k in range(1, rollMax[j] + 1):
                    if i - k < 0:
                        break
                    dp[i][j] += dp[i - k][6] - dp[i - k][j]
            dp[i][6] = sum(dp[i])

        return dp[n][6] % 1000000007
