class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        helper_grid = [[0] * (len(grid[0])) for _ in range(len(grid))]
        helper_grid[max_row][max_col] = grid[max_row][max_col]
        for i in range(max_col - 1, -1, -1):
            helper_grid[max_row][i] = grid[max_row][i] + helper_grid[max_row][i + 1]
        for i in range(max_row - 1, -1, -1):
            helper_grid[i][max_col] = grid[i][max_col] + helper_grid[i + 1][max_col]

        for col in range(max_col - 1, -1, -1):
            for row in range(max_row - 1, -1, -1):
                helper_grid[row][col] = grid[row][col] + min(helper_grid[row + 1][col], helper_grid[row][col + 1])
        return helper_grid[0][0]
