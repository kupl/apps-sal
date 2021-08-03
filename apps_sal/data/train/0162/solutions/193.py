class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * (len(text2) + 1) for i in range(len(text1) + 1)]

        def LCS(s1, s2, n, m, dp):
            if n == 0 or m == 0:
                return 0
            if dp[n - 1][m - 1] != -1:
                return dp[n - 1][m - 1]
            if s1[n - 1] == s2[m - 1]:
                dp[n - 1][m - 1] = 1 + LCS(s1, s2, n - 1, m - 1, dp)
                return dp[n - 1][m - 1]
            else:
                dp[n - 1][m - 1] = max(LCS(s1, s2, n - 1, m, dp), LCS(s1, s2, n, m - 1, dp))
                return dp[n - 1][m - 1]

        return (LCS(text1, text2, len(text1), len(text2), dp))
