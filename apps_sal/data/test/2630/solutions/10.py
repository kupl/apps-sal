class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not len(obstacleGrid) > 0:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        arr = [[1 for y in range(n)] for x in range(m)]
        for x in range(m):
            for y in range(n):
                if x == 0:
                    arr[x][y] = arr[x][y - 1]
                elif y == 0:
                    arr[x][y] = arr[x - 1][y]
                else:
                    arr[x][y] = arr[x - 1][y] + arr[x][y - 1]
                if obstacleGrid[x][y] == 1:
                    arr[x][y] = 0
        return arr[-1][-1]
