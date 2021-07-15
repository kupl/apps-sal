class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        if not text1 or not text2: return 0
        dp = [[0 for i in range(len(text1))] for j in range(len(text2))]
        for i in range(len(text2)):
            for j in range(len(text1)):
                if i == 0 and j == 0:
                    dp[i][j] = 1 if text1[j] == text2[i] else 0
                elif i == 0:
                    if dp[i][j-1] == 0 and text1[j] == text2[i]: dp[i][j] = 1
                    else: dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = 1 if dp[i-1][j] == 1 or text1[j] == text2[i] else 0
                elif text1[j] == text2[i]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
