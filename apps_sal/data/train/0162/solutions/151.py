class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [-1] * len(text1)
        for i in range(len(dp)):
            dp[i] = [-1] * len(text2)

        self.dp = dp
        self.t1 = text1
        self.t2 = text2

        return self.LCSHelper(len(text1) - 1, len(text2) - 1)

    def LCSHelper(self, i, j):
        if i < 0 or i >= len(self.t1) or j < 0 or j >= len(self.t2):
            return 0

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        if self.t1[i:i + 1] == self.t2[j:j + 1]:
            self.dp[i][j] = 1 + self.LCSHelper(i - 1, j - 1)
        else:
            self.dp[i][j] = max(self.LCSHelper(i, j - 1), self.LCSHelper(i - 1, j))

        return self.dp[i][j]
