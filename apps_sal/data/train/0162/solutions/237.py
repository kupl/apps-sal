class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dynamic_array = [[0 for c in range(len(text2) + 1)] for ch in range(len(text1) + 1)]

        for i in range(len(text1) + 1):
            for j in range(len(text2) + 1):

                if i == 0 or j == 0:
                    dynamic_array[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    dynamic_array[i][j] = 1 + dynamic_array[i - 1][j - 1]
                else:
                    dynamic_array[i][j] = max(dynamic_array[i - 1][j], dynamic_array[i][j - 1])

        return dynamic_array[len(text1)][len(text2)]
