class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target == d or target == d * f:
            return 1
        T = [[0 for j in range(target + 1)] for i in range(d + 1)]
        m = 10 ** 9 + 7
        T[0][0] = 1
        for i in range(1, d + 1):
            T[i][0] = 0
            for j in range(1, target + 1, 1):
                for k in range(1, f + 1):
                    if j >= k:
                        T[i][j] += T[i - 1][j - k] % m
                        T[i][j] %= m
        return T[d][target] % m
