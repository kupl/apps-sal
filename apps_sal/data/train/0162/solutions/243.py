class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2))] for i in range(len(text1))]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    if not i or not j:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    if i:
                        dp[i][j] = dp[i - 1][j]
                    if j:
                        dp[i][j] = max(dp[i][j], dp[i][j - 1])
        return dp[-1][-1]
