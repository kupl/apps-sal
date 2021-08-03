class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        D = []
        for i in range(len(text1) + 1):
            D.append([0] * (len(text2) + 1))

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                delta = 1 if text1[i - 1] == text2[j - 1] else 0
                D[i][j] = max(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1] + delta)

        return D[len(text1)][len(text2)]
