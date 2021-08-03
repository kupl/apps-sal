class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.find({}, 0, 0, text1, text2)

    def find(self, memo, i, j, text1, text2):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == len(text1):
            return 0
        if j == len(text2):
            return 0
        if text1[i] == text2[j]:
            memo[(i, j)] = self.find(memo, i + 1, j + 1, text1, text2) + 1
        else:
            memo[(i, j)] = max(self.find(memo, i, j + 1, text1, text2), self.find(memo, i + 1, j, text1, text2))
        return memo[(i, j)]
