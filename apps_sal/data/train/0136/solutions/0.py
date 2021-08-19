class Solution:

    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        INF = -10000
        n = len(grid)
        total = 0
        max_rows = [max(row, default=INF) for row in grid]
        max_cols = [max(col, default=INF) for col in zip(*grid)]
        for (i, best_row) in enumerate(max_rows):
            for (j, best_col) in enumerate(max_cols):
                new_height = min(best_row, best_col)
                total += new_height - grid[i][j]
        return total
