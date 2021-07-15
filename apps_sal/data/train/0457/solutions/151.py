class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [0] + [amount+1 for i in range(amount)]
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i-c]+1, dp[i])
                    
        return dp[amount] if dp[amount] < amount+1 else -1
    
    

#     def coinChange(self, coins: List[int], amount: int) -> int:
#         n = len(coins)
#         dp = [[amount+1 for j in range(n+1)] for i in range(amount+1)]
#         for j in range(n+1):
#             dp[0][j] = 0
#         for i in range(1, amount+1):
#             for j in range(1, n+1):
#                 if coins[j-1] > i:
#                     dp[i][j] = dp[i][j-1]
#                 else:
#                     dp[i][j] = min(dp[i-coins[j-1]][j]+1, dp[i][j-1])
            
#         return dp[amount][n] if dp[amount][n] < amount+1 else -1

