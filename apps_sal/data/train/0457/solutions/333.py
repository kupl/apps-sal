class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        if n == 0:
            return 0
        dp = [[amount + 1] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j - coins[i - 1] >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - coins[i - 1]] + 1)
        return dp[n][amount] if dp[n][amount] <= amount else -1
