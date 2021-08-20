class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        dp = [[0 for col in range(len(text2) + 1)] for row in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                options = [dp[i][j - 1], dp[i - 1][j]]
                if text1[i - 1] == text2[j - 1]:
                    options.append(dp[i - 1][j - 1] + 1)
                dp[i][j] = max(options)
        return dp[-1][-1]
