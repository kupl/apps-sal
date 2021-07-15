class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        str1, str2 = text1, text2

        num_rows = len(str1) + 1
        num_cols = len(str2) + 1
        lengths = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        for row in range(1, num_rows):
            for col in range(1, num_cols):
                if str1[row - 1] == str2[col - 1]:
                    lengths[row][col] = lengths[row - 1][col - 1] + 1
                else:
                    lengths[row][col] = max(lengths[row - 1][col], lengths[row][col - 1])

        return lengths[-1][-1]

