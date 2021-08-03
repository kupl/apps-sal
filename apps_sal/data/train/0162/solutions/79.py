class Solution:
    def lcs(self, text1, text2, i1, i2, memo):
        if len(text1) == i1 or len(text2) == i2:
            return 0

        if memo[i1][i2] != -1:
            return memo[i1][i2]

        if text1[i1] == text2[i2]:
            memo[i1][i2] = 1 + self.lcs(text1, text2, i1 + 1, i2 + 1, memo)
            return memo[i1][i2]

        maxLen = 0
        maxLen = max(maxLen, self.lcs(text1, text2, i1 + 1, i2, memo))
        maxLen = max(maxLen, self.lcs(text1, text2, i1, i2 + 1, memo))
        memo[i1][i2] = maxLen

        return maxLen

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        maxLen = self.lcs(text1, text2, 0, 0, memo)
        return maxLen
