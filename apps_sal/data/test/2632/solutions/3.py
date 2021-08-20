class Solution:

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid) - 1
        n = len(grid[0]) - 1
        dic = dict()
        s = self.minPathSumHelper(grid, 0, 0, m, n, dic)
        return s

    def minPathSumHelper(self, grid, i, j, m, n, dic):
        if (i, j, m, n) in dic:
            return dic[i, j, m, n]
        if i > m or j > n:
            return 0
        elif i == m:
            dic[i, j, m, n] = self.minPathSumHelper(grid, i, j + 1, m, n, dic) + grid[i][j]
            return dic[i, j, m, n]
        elif j == n:
            dic[i, j, m, n] = self.minPathSumHelper(grid, i + 1, j, m, n, dic) + grid[i][j]
            return dic[i, j, m, n]
        else:
            dic[i, j, m, n] = min(self.minPathSumHelper(grid, i + 1, j, m, n, dic), self.minPathSumHelper(grid, i, j + 1, m, n, dic)) + grid[i][j]
            return dic[i, j, m, n]
