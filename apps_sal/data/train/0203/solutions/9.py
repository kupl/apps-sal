class Solution:

    def uniquePaths(self, m, n, memo=None):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 and n == 1:
            return 1
        if m < 1 or n < 1:
            return 0
        if not memo:
            memo = [[0 for i in range(n + 1)] for j in range(m + 1)]
        if memo[m][n]:
            return memo[m][n]
        else:
            memo[m][n] = self.uniquePaths(m - 1, n, memo) + self.uniquePaths(m, n - 1, memo)
            return memo[m][n]
