class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        P = [[0 for j in range(n + 1)] for i in range(m + 1)]
        P[0][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if obstacleGrid[i - 1][j - 1] != 1:
                    P[i][j] = P[i - 1][j] + P[i][j - 1]
        return P[m][n]
