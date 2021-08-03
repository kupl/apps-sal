class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        matrix = [[0 for j in range(n)] for i in range(m)]

        matrix[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    matrix[i][j] = matrix[i][j - 1]
                elif j == 0:
                    matrix[i][j] = matrix[i - 1][j]
                else:
                    matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]
        return matrix[m - 1][n - 1]
