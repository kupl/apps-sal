class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], 1 + dp[j - coin])
        return dp[-1] if dp[-1] != float('inf') else -1
