class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(i,j):
            if i==len(text1) or j==len(text2):
                return 0
            if tuple([i,j]) in dp:
                return dp[tuple([i,j])]
            if text1[i]==text2[j]:
                dp[tuple([i,j])]=1+lcs(i+1,j+1)
                return dp[tuple([i,j])]
            dp[tuple([i,j])]=max(lcs(i+1,j),lcs(i,j+1))
            return dp[tuple([i,j])]
        dp={}
        # text1+=\"0\"
        # text2+=\"0\"
        return lcs(0,0)
