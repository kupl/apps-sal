class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf') for j in range(n + 1)] for i in range(amount + 1)]
        for j in range(n + 1):
            dp[0][j] = 0
        for i in range(1, amount + 1):
            for j in range(1, n + 1):
                c = coins[j - 1]
                if c > i:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = min(dp[i - c][j] + 1, dp[i][j - 1])
        return dp[amount][n] if dp[amount][n] < amount + 1 else -1
