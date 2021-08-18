class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ways = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    ways[i][j] = 0
                elif i == 0 and j == 0:
                    ways[i][j] = 1
                elif i == 0:
                    ways[i][j] = ways[i][j - 1]
                elif j == 0:
                    ways[i][j] = ways[i - 1][j]
                else:
                    ways[i][j] = ways[i - 1][j] + ways[i][j - 1]
        return ways[m - 1][n - 1]
