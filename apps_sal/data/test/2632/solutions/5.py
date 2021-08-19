class Solution:

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        row_count = len(grid)
        col_count = len(grid[0])
        for i in range(1, row_count):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, col_count):
            grid[0][i] += grid[0][i - 1]
        for row in range(1, row_count):
            for col in range(1, col_count):
                grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
        return grid[-1][-1]
