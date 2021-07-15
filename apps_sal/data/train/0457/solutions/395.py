class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     coins = set(coins)
    #     dp = [float('inf') if i not in coins else 1 for i in range(amount+1)]
    #     dp[0] = 0
    #     for coin in coins:
    #         for i in range(coin, amount+1):
    #             dp[i] = min(dp[i], dp[i-coin]+1)
    #     return -1 if dp[amount] == float('inf') else dp[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = set(coins)
        dp = [float('inf') if i not in coins else 1 for i in range(amount+1)]
        result = self.helper(coins, amount,dp) 
        return -1 if result == float('inf') else result
    
    def helper(self,coins, amount, dp):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if dp[amount] != float('inf'):
            return dp[amount]
        current_min = float('inf')
        for coin in coins: 
            result = self.helper(coins,amount-coin,dp)
            if result != -1:
                current_min = min(current_min, 1+result)
        if current_min == float('inf'):
            dp[amount] = -1
            return -1
        dp[amount] = current_min
        return current_min
        

