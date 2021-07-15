class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1
        Max = amount + 1
        dp = [Max] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if (coins[j] <= i):
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        
        if amount < dp[amount]:
            return -1
        return dp[amount]
