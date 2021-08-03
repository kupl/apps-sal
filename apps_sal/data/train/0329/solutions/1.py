class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if (rows == 0):
            return -1

        cols = len(grid[0])
        if (cols == 0):
            return -1

        dp = [(1, 1)] * cols

        for r, col in enumerate(grid):
            for c, item in enumerate(col):
                if (r == 0 and c == 0):
                    dp[c] = (item, item)
                elif (r == 0):
                    dp[c] = (dp[c - 1][0] * item, dp[c - 1][1] * item)
                elif (c == 0):
                    dp[c] = (dp[c][0] * item, dp[c][1] * item)
                else:
                    c1 = dp[c - 1][0] * item
                    c2 = dp[c - 1][1] * item
                    c3 = dp[c][0] * item
                    c4 = dp[c][1] * item

                    m = min(dp[c - 1][0] * item, dp[c - 1][1] * item, dp[c][0] * item, dp[c][1] * item)
                    M = max(dp[c - 1][0] * item, dp[c - 1][1] * item, dp[c][0] * item, dp[c][1] * item)
                    dp[c] = (m, M)

        if (dp[cols - 1][1] >= 0):
            return (dp[cols - 1][1] % (10**9 + 7))
        else:
            return -1
