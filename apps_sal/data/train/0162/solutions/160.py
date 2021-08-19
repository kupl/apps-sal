class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        self.dp(text1, text2, len(text1) - 1, len(text2) - 1, memo)
        return memo[len(text1) - 1, len(text2) - 1]

    def dp(self, text1, text2, i, j, memo):
        if i == -1 or j == -1:
            return 0
        if (i, j) in memo:
            return memo[i, j]
        if text1[i] == text2[j]:
            memo[i, j] = self.dp(text1, text2, i - 1, j - 1, memo) + 1
            return memo[i, j]
        else:
            memo[i, j] = max(self.dp(text1, text2, i - 1, j, memo), self.dp(text1, text2, i, j - 1, memo))
            return memo[i, j]
        return memo[i, j]
