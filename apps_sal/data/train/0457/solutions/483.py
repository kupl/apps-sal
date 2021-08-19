class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[sys.maxsize] * (amount + 1), [sys.maxsize] * (amount + 1)]
        for i in range(1, n + 1):
            dp[i % 2][0] = 0
            for j in range(1, amount + 1):
                dp[i % 2][j] = dp[(i - 1) % 2][j]
                if coins[i - 1] <= j:
                    dp[i % 2][j] = min(dp[i % 2][j - coins[i - 1]] + 1, dp[i % 2][j])
        return dp[n % 2][amount] if dp[n % 2][amount] < sys.maxsize else -1
