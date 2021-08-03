class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0

#         grid = [[[None, 0, None, None] for i in range(len(text1) + 1)] for i in range(len(text2) + 1)]

#         for i in range(1, len(text2) + 1):
#             for j in range(1, len(text1) + 1):
#                 if text1[j - 1] == text2[i - 1]:
#                     grid[i][j] = [text2[i - 1], grid[i - 1][j - 1][1] + 1, i - 1, j - 1]
#                 else:
#                     if grid[i - 1][j][1] > grid[i][j - 1][1]:
#                         grid[i][j] = [None, grid[i - 1][j][1], i - 1, j]
#                     else:
#                         grid[i][j] = [None, grid[i][j - 1][1], i, j - 1]
#         return grid[-1][-1][1]

        grid = [[[0] for i in range(len(text1) + 1)] for i in range(len(text2) + 1)]

        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text1[j - 1] == text2[i - 1]:
                    grid[i][j] = [grid[i - 1][j - 1][0] + 1]
                else:
                    if grid[i - 1][j] > grid[i][j - 1]:
                        grid[i][j] = grid[i - 1][j]
                    else:
                        grid[i][j] = grid[i][j - 1]
        return grid[-1][-1][0]
