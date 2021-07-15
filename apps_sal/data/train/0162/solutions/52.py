class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = defaultdict(int)
        for i, c1 in enumerate(text1):
            for j, c2 in enumerate(text2):
                dp[i,j]  = max(dp[i-1, j-1] + (c1==c2), dp[i-1,j], dp[i,j-1])
                
        return dp[len(text1)-1, len(text2)-1]
