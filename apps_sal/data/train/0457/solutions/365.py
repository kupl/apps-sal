class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf') for i in range(amount+1)] for i in range(len(coins))]
        
        for amount in range(len(dp[0])):
            if amount % coins[0]  == 0:
                dp[0][amount] = amount // coins[0]
        
        for coin in range(len(dp)):
            dp[coin][0] = 0
            
            
        
        for coin in range(1, len(dp)):
            for amount in range(1, len(dp[0])):
                if amount >= coins[coin]:
                    dp[coin][amount] = min(dp[coin][amount-coins[coin]]+1, dp[coin-1][amount])
                else:
                    dp[coin][amount] = dp[coin-1][amount]
        
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
