class Solution:

    def knightDialer(self, N: int) -> int:
        maxs = 10 ** 9 + 7
        moves = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
        memo = {}
        neighbors = {1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (3, 9, 0), 5: tuple(), 6: (1, 7, 0), 7: (2, 6), 8: (1, 3), 9: (2, 4), 0: (4, 6)}

        def dfs(i, n):
            if n == 1:
                return 1
            if (n, i) in memo:
                return memo[n, i]
            else:
                nums = 0
                for d in neighbors[i]:
                    nums += dfs(d, n - 1)
                memo[n, i] = nums
            return nums
        total = 0
        for i in range(10):
            total += dfs(i, N)
        return total % maxs
