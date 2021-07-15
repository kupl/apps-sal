class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp= [[0]*(len(text2)+1) for _ in range((len(text1)+1))]
        count=0
        for r in range(1, len(dp)):
            for c in range(1, len(dp[0])):
                if text1[r-1]==text2[c-1]:
                    dp[r][c]= dp[r-1][c-1]+1
                else:
                    dp[r][c]= max(dp[r-1][c], dp[r][c-1])
                    
                count= max(count,dp[r][c])
                
        return count

