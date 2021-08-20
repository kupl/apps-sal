class Solution:

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        s = [[0 for j in range(n)] for i in range(m)]
        s[0][0] = grid[0][0]
        for i in range(1, m):
            s[i][0] = s[i - 1][0] + grid[i][0]
        for j in range(1, n):
            s[0][j] = s[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                s[i][j] = min(s[i - 1][j] + grid[i][j], s[i][j - 1] + grid[i][j])
        return s[m - 1][n - 1]
