class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = dict()
        return self.top_down(dp, text1, text2, 0, 0)

    def recursive(self, text1, text2, i, j):
        if i >= len(text1) or j >= len(text2):
            return 0
        if text1[i] == text2[j]:
            return 1 + self.recursive(text1, text2, i + 1, j + 1)
        a = self.recursive(text1, text2, i + 1, j)
        b = self.recursive(text1, text2, i, j + 1)
        return max(a, b)

    def top_down(self, dp, text1, text2, i, j):
        if i >= len(text1) or j >= len(text2):
            return 0
        if text1[i] == text2[j]:
            return 1 + self.top_down(dp, text1, text2, i + 1, j + 1)
        if (i, j) in dp:
            return dp[i, j]
        a = self.top_down(dp, text1, text2, i + 1, j)
        b = self.top_down(dp, text1, text2, i, j + 1)
        dp[i, j] = max(a, b)
        return dp[i, j]

    def bottom_up(self, text1, text2):
        (i, j) = (0, 0)
        (m, n) = (len(text1), len(text2))
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
