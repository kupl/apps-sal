class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        n = target
        ways = [[0 for i in range(n + 1)] for j in range(d + 1)]
        ways[0][0] = 1
        for i in range(1, d + 1):
            for j in range(n + 1):
                c = 0
                for k in range(1, f + 1):
                    c += ways[i - 1][j - k] if j - k >= 0 else 0
                ways[i][j] = c
        return ways[d][n] % (10 ** 9 + 7)
