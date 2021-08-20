class Solution:

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """

        def dfs(n):
            if n == 1:
                return 0
            if n == 3:
                return 2
            if n & 1 == 0:
                return dfs(n >> 1) + 1
            elif n >> 1 & 1 == 0:
                return dfs(n - 1) + 1
            else:
                return dfs(n + 1) + 1
        return dfs(n)
