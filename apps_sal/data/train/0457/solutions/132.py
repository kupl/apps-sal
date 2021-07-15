class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
#        1 2 3 4 5 6 7 8 9 10 11
#      0 
# 1    0 1 1 2 2 1 2 2 3 4 2 3
# 2    0   1 2     
# 5    0  
        dp = [float('inf')] * (amount+1)
        dp[0] = 0 

        for i in range(1,amount+1):
            for c in coins:
                if c<=i:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        
        return dp[-1] if dp[-1] != float('inf') else -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # sort list descedning order
    
#     coins = [1,2,5] 1 + 4 = 5 -> coinchange(4) + 1
#                     2 + 3 = 5 -> coinchange(3) + 1
#                     5 + 0 = 5 -> coinchange(0) + 1
           
#     amount                 0  1  2  3  4. 5..  10 11
        
#     fewest num of coins    0  1  1  2 2  min()
            
#         coin in coins
#             if amount != coin:
#                 dp[amount] = dp[amount-coin] + 1
                                
        
#         def dfs(amount):
            
#             # Have we solved this before
#             if amount in memo:
#                 return memo[amount]
            
#             # recursive base case
#             if amount == 0:
#                 return 0
            
#             # find all cases
#             tmp = []
#             for i in range(len(coins)):
                
#                 if amount - coins[i] >= 0:
#                     tmp.append(dfs(amount-coins[i],))
                    
#                 else:
#                     tmp.append(float('inf'))
                
            
#             # save the output in memory
#             _min = min(tmp) + 1
#             memo[amount] = _min
            
#             return _min
        
# #         memo = {}
# #         output = dfs(amount)
        
# #         return output if output != float('inf') else -1
#         dp = [float('inf')] * (amount + 1)
#         dp[0] = 0
#         for coin in coins:
#             for x in range(coin, amount+1):
#                 dp[x] = min(dp[x],dp[x-coin]+1)
        
#         return dp[amount] if dp[amount] != float('inf') else -1
        
    
        

