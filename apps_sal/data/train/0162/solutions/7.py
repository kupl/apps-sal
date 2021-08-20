class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        (m, n) = (len(text1), len(text2))
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i != 0 and j != 0:
                    if text1[i - 1] == text2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    dp[i][j] = max(dp[i][j], max(dp[i - 1][j], dp[i][j - 1]))
        return dp[-1][-1]
