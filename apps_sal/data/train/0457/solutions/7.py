class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for a in range(coin, amount + 1):
                if dp[a - coin] >= dp[a]:
                    continue
                dp[a] = dp[a - coin] + 1
        return dp[amount] if dp[amount] < float('inf') else -1

