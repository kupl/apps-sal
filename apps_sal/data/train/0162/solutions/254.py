class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j]
        # represents what is the maximum up to that i and j included
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        max_ = 0
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i + 1][j + 1] + 1, dp[i][j])
                max_ = max(max_, dp[i][j])
        return max_
