class Solution:

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        sol = [[0 for j in range(n)] for i in range(m)]
        sol[0][0] = 1
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 or j == 0:
                    sol[i][j] = 1
                else:
                    sol[i][j] = sol[i - 1][j] + sol[i][j - 1]
        return sol[-1][-1]
