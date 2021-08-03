class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if 0 in (m, n):
            return 0
        results = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                results[i][j] = results[i - 1][j] + results[i][j - 1]
        return results[m - 1][n - 1]
