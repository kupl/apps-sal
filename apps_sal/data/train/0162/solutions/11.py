class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        def print_grid(grid):
            for row in grid:
                print(row)

        dp_row = [0] * (len(s2) + 1)
        dp_row_pre = [0] * (len(s2) + 1)
        N, M = len(s1), len(s2)
        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp_row[j] = dp_row_pre[j + 1] + 1
                else:
                    dp_row[j] = max(dp_row_pre[j], dp_row[j + 1])
            dp_row_pre, dp_row = dp_row, dp_row_pre
        return dp_row_pre[0]
