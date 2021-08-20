class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2))] for i in range(len(text1))]
        dp[0][0] = int(text1[0] == text2[0])
        for i in range(1, len(text1)):
            dp[i][0] = max(int(text1[i] == text2[0]), dp[i - 1][0])
        for j in range(1, len(text2)):
            dp[0][j] = max(int(text2[j] == text1[0]), dp[0][j - 1])
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        print(dp)
        return dp[-1][-1]
