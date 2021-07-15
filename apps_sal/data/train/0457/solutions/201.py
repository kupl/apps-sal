class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # dp[n] means minimal coin number to gather n amount of money
        dp[0] = 0
        
        for i in range(len(dp)):
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1
