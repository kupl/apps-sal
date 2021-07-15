class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        for i in range(amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], 1 + dp[i-coins[j]])
                
        if dp[amount] > amount:
            return -1
        return dp[amount]
        

