class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        #dp[i] = min (dp[i - c1], dp[i - c2], ...) + 1
        dp[0] = 0

        for coin in coins:
            for i in range(coin, len(dp)):
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
        return dp[amount] if dp[amount] != float('inf') else -1
