class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n = len(text1)
        m = len(text2)
        
        dp = []
        
        for i in range(n):
            dp.append([-1]*m)
        
        def lcs(i,j):
            
            if(i>=n or j>=m):
                return 0
            
            if(dp[i][j]!=-1):
                return dp[i][j]
            
            if(text1[i]==text2[j]):
                ans = 1 + lcs(i+1,j+1)
            else:
                ans = max(lcs(i+1,j),lcs(i,j+1))
            
            dp[i][j] = ans
            
            return ans
        return lcs(0,0)

