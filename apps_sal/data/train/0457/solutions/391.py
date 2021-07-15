class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         n = len(coins)
#         return self.coinChangeHelper(coins, n, amount, {})
        
    
#                #            11
#                #   10       9        6  => 
#                # 9 8 5   8 7 4    5 4 1 => 1
#                #                      0 => 0
#     def coinChangeHelper(self, coins, n, amount, mem):
#         if amount in mem:
#             return mem[amount]
#         if amount == 0:
#             return 0
#         if n == 0:
#             return -1
        
#         minCoins = math.inf
#         for i in range(n):
#             if coins[i] <= amount:
#                 numCoins = self.coinChangeHelper(coins, n, amount - coins[i], mem)
#                 if numCoins != -1:
#                     minCoins = min(minCoins, numCoins)
        
#         if minCoins == math.inf:
#             mem[amount] = -1
#         else:
#             mem[amount] = minCoins + 1
        
#         return mem[amount]
#     [1, 2, 5], amount = 11
    
#      0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27
#  2   0   -1  1   -1  2   -1  3  -1   4   -1  5   -1   6  -1  7   -1  8   -1  9   -1  10  -1  11   
#  5   0   -1  1  -1   2   1   3   2   
# 10
#  1
    
    # if coins[i] <= j: dp[i][j] = min(dp[i][j-coins[i]] + 1, dp[i-1][j])
    # else: dp[i][j] = dp[i-1][j]
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
    
        dp = [[0 for j in range(amount + 1)] for i in range(n)]
        
        for j in range(amount + 1):
            dp[0][j] = -1 if j % coins[0] else j // coins[0]
            
        for i in range(1, n):
            for j in range(1, amount + 1):
                includeDenom = -1 if coins[i] > j else dp[i][j-coins[i]]
                excludeDenom = dp[i-1][j]
                if includeDenom == -1 and excludeDenom == -1:
                    dp[i][j] = -1
                elif includeDenom == -1:
                    dp[i][j] = excludeDenom
                elif excludeDenom == -1:
                    dp[i][j] = includeDenom + 1
                else:
                    dp[i][j] = min(includeDenom + 1, excludeDenom)
                    
        return dp[n-1][amount]
                    

