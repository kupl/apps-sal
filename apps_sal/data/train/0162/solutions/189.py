import numpy as np
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        best = np.zeros((n+1,m+1))
        ans = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                
                if text1[i-1]==text2[j-1]:
                    best[i][j] = best[i-1][j-1] + 1
                else:
                    best[i][j] = max(best[i-1][j],best[i][j-1])
                    
                ans = max(ans,best[i][j])
                
        return int(ans)
