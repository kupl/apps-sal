class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        mat = [[0] * n for _ in range(m)]
        if not obstacleGrid[0][0]:
            mat[0][0] = 1
        for row in range(m):
            for col in range(n):
                if col == 0 and row == 0:
                    mat[row][col] = obstacleGrid[row][col] * -1 + 1
                elif obstacleGrid[row][col] == 1:
                    mat[row][col] == 0
                else:
                    mat[row][col] = mat[row - 1][col] + mat[row][col - 1]
        return mat[m - 1][n - 1]
