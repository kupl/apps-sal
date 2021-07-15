class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:    
        def lcsTab(s1,s2,m,n):
            dp = [[0 for i in range(n+1)] for j in range(m+1)]
            
            for i in range(m+1):
                for j in range(n+1):
                    if(i==0 or j==0):
                        dp[i][j] = 0
                    elif(s1[i-1] == s2[j-1]):
                        dp[i][j] = 1+dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            
            return dp[m][n]
            
        m = len(text1)
        n = len(text2)
        
        return lcsTab(text1,text2,m,n)
        

