class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        matrix = [0] * (len(text2) + 1)
        for i in range(1, len(text1) + 1):
            p = 0
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    p, matrix[j] = matrix[j], 1 + p
                else:
                    p, matrix[j] = matrix[j], max(matrix[j], matrix[j - 1])
        return matrix[len(text2)]
