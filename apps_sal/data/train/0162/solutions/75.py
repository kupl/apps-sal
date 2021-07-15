from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
#         @lru_cache(maxsize=None)
#         def recur(n,m):
            
#             if n == len(text1) or m == len(text2):
#                 return 0
            
#             if text1[n] == text2[m]:
#                 return 1 + recur(n+1,m+1)
            
#             else:
            
#                 return max(recur(n,m+1),recur(n+1,m))
                
        
#         return recur(0,0)
        
    #    '' a b c d e
    # '' 0  0 0 0 0 0 
    # a  0  1 1 1 1 1
    # c  0  1 1 2 2 2
    # e  0  1 1 2 2 3
    
        # dp = [[0]*(len(text1)+1) for _ in range(len(text2)+1)]
        
        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text1) + 1)
        # print(len(dp),len(dp[0]))
        
        for i in range(1,len(text2)+1):
            for j in range(1,len(text1)+1):
                
                if text2[i-1] == text1[j-1]:
                    
                    current[j] = previous[j-1] + 1
                else:
                    current[j] = max(current[j-1], previous[j])
                
            previous = current
            current = [0] * (len(text1) + 1)
                
        return previous[-1]









#         dp_grid = [[0]*(len(text1)+1) for _ in range(len(text2)+1)]
      
#         for row in range(len(text2)):
#             for col in range(len(text1)):
#                 # print(row,col)
#                 if text1[col] == text2[row]:
#                     dp_grid[row+1][col+1] = 1 + dp_grid[row][col]
#                 else:
#                     dp_grid[row+1][col+1] = max(dp_grid[row][col+1],dp_grid[row+1][col])
        
#         return dp_grid[len(text2)][len(text1)]
                    

