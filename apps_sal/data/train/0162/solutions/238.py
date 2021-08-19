class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        dp = [[0 for c in range(l2 + 1)] for r in range(l1 + 1)]
        for i in range(l1):
            for j in range(l2):
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], dp[i][j] + (text1[i] == text2[j]))
        return dp[-1][-1]
