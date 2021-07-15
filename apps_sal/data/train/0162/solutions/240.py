class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[-1 for i in range(len(text2)+1)]for j in range(len(text1)+1)]
        for i in range(len(text1)+1):
            for j in range(len(text2)+1):
                if i==0 or j==0:
                    dp[i][j]=0
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[len(text1)][len(text2)]
