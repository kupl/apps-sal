class Solution:

    def knightDialer(self, N: int) -> int:
        memo = {}
        maxi = 10 ** 9 + 7

        def paths(i, j, n):
            if i > 3 or j > 2 or i < 0 or (j < 0) or (i == 3 and j != 1):
                return 0
            if n == 1:
                return 1
            if (i, j, n) in memo:
                return memo[i, j, n]
            result = paths(i - 1, j - 2, n - 1) % maxi + paths(i - 2, j - 1, n - 1) % maxi + paths(i - 2, j + 1, n - 1) % maxi + paths(i - 1, j + 2, n - 1) % maxi + paths(i + 1, j + 2, n - 1) % maxi + paths(i + 2, j + 1, n - 1) % maxi + paths(i + 2, j - 1, n - 1) % maxi + paths(i + 1, j - 2, n - 1) % maxi
            memo[i, j, n] = result
            return result
        totalPaths = 0
        for i in range(4):
            for j in range(3):
                totalPaths = (totalPaths + paths(i, j, N)) % maxi
        return totalPaths
