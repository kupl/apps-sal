class Solution:
    def lcs(self, s1, s2, m, n):
        if m == 0 or n == 0:
            return 0
        if self.dp[m][n] != -1: return self.dp[m][n]
        if s1[m - 1] == s2[n - 1]:
            self.dp[m][n] = 1 + self.lcs(s1, s2, m - 1, n - 1)
        else:
            self.dp[m][n] = max(self.lcs(s1, s2, m - 1, n), self.lcs(s1, s2, m, n - 1))
        return self.dp[m][n]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        self.dp = [[-1 for _ in range(n + 1)] for __ in range(m + 1)]
        return self.lcs(text1, text2, m, n)

