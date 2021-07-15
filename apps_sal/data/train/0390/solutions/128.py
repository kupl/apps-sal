class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = {0: False}
        def dfs(i):
            if i not in memo:
                memo[i] = False
                j = 1
                while not memo[i] and j * j <= i:
                    memo[i] = not dfs(i - j * j)
                    j += 1
            return memo[i]
        
        return dfs(n)
        
        
        
        
#         dp = [False] * (n + 1)
#         for i in range(1, n + 1):
#             j = 1
#             while not dp[i] and j * j <= i:
#                 dp[i] = not dp[i - j * j]
#                 j += 1
        
#         return dp[n]
                
            

