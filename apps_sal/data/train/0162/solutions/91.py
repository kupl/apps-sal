class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.lcs(text1, text2, len(text1) - 1, len(text2) - 1, {})

    def lcs(self, text1, text2, i, j, memo):
        if i < 0 or j < 0:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        if text1[i] == text2[j]:
            return 1 + self.lcs(text1, text2, i - 1, j - 1, memo)

        memo[(i, j)] = max(
            self.lcs(text1, text2, i - 1, j, memo),
            self.lcs(text1, text2, i, j - 1, memo),
        )

        return memo[(i, j)]
