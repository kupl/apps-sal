class Solution:

    def __init__(self):
        self.dp = None

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.dp = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        return self.lcs_rec(text1, text2, len(text1), len(text2))

    def lcs_rec(self, x, y, n, m):
        if n == 0 or m == 0:
            return 0
        if self.dp[n][m] != -1:
            return self.dp[n][m]
        if x[n - 1] == y[m - 1]:
            self.dp[n][m] = 1 + self.lcs_rec(x, y, n - 1, m - 1)
        else:
            self.dp[n][m] = max(self.lcs_rec(x, y, n - 1, m), self.lcs_rec(x, y, n, m - 1))
        return self.dp[n][m]
