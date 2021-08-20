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
        return max(a, b)
