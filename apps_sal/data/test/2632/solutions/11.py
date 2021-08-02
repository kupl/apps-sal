class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col = len(grid[0])
        row = len(grid)
        minSum = [[0 for x in range(col)] for y in range(row)]

        for i in range(row):
            for j in range(col):
                add = 0
                if i - 1 >= 0 and j - 1 >= 0:
                    add = min(minSum[i - 1][j], minSum[i][j - 1])
                elif i - 1 >= 0:
                    add = minSum[i - 1][j]
                elif j - 1 >= 0:
                    add = minSum[i][j - 1]
                minSum[i][j] = grid[i][j] + add

        return minSum[-1][-1]
