# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp=[float('inf')]*(amount+1)
#         dp[0]=0
        
#         for i in range(1, amount+1):
#             for c in coins:
#                 if c<=i:        #check if coin value fits in current amount i
#                     dp[i]=min(dp[i], dp[i-c]+1)
        
#         if dp[amount]>amount:
#             return -1
#         else:
#             return dp[amount]
                    
    
    
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i]=min(dp[i], dp[i-coin]+1)
                
        return dp[amount] if dp[amount] !=float('inf') else -1
