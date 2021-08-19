class Solution:

    def paths(self, obstacleGrid, n, m, a, b, memo):
        if n > a or m > b:
            return 0
        if obstacleGrid[n][m] == 1:
            return 0
        if n == a and m == b:
            return 1
        if str(n) + ' ' + str(m) not in memo:
            memo[str(n) + ' ' + str(m)] = self.paths(obstacleGrid, n + 1, m, a, b, memo) + self.paths(obstacleGrid, n, m + 1, a, b, memo)
        return memo[str(n) + ' ' + str(m)]

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        a = len(obstacleGrid)
        b = len(obstacleGrid[0])
        memo = dict()
        return self.paths(obstacleGrid, 0, 0, a - 1, b - 1, memo)
