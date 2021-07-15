import numpy as np
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        l1 = len(text1)
        l2 = len(text2)
        
        dp = np.zeros((l1+1, l2+1), dtype = int)
        
    
        dp[:][0] = 0
        
  
        dp[0][:] = 0
            
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[-1][-1]
        
        

