class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        if M == 0:
            return 0
        N = len(grid[0])
        if N == 0:
            return 0

        INF = float('inf')
        mem = {}

        def min_path(i, j):
            if i == M - 1 and j == N - 1:
                return grid[i][j]
            if (i, j) in mem:
                return mem[(i, j)]

            min_sum = INF
            if i < M - 1:
                min_sum = min_path(i + 1, j)
            if j < N - 1:
                min_sum = min(min_sum, min_path(i, j + 1))

            mem[(i, j)] = grid[i][j] + min_sum
            return mem[(i, j)]

        return min_path(0, 0)
