class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

#         dp = [[0] * 7 for _ in range(n)]
#         dp[0] = [1] * 6 + [6]
        
#         for j in range(1, n):
#             for i in range(6):
                
#                 dp[j][i] = dp[j - 1][-1]
#                 k = j - rollMax[i]
                
#                 if k == 0:
#                     dp[j][i] -= 1
                
#                 elif k > 0:
#                     dp[j][i] -= (dp[k - 1][-1] - dp[k - 1][i])
                    
#                 # dp[i][-1] += dp[i][j]
#             dp[i][6] = sum(dp[i][:6])
                
#         print (dp)
                
#         return dp[n-1][len(rollMax)] % int(1e9 + 7)
        

        dp = [[0] * 7 for _ in range(n)]
        dp[0] = [1] * 6 + [6]

        for r in range(1, n):
            for c in range(6):
                
                dp[r][c] = dp[r-1][-1]
                
                k = r - rollMax[c]

                if k == 0: # when all numbers = i
                    dp[r][c] -= 1
                    
                elif k >= 1: # when we have prefix
                    dp[r][c] -= (dp[k-1][-1] - dp[k-1][c])
                
            dp[r][6] = sum(dp[r][:6])
            
        # print (dp)
            
        return dp[-1][-1] % int(1e9 + 7)
                    

