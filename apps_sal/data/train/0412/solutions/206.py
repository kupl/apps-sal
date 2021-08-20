class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        m = pow(10, 9) + 7
        T = [[0 for i in range(max(target + 1, f + 1))] for i in range(d)]
        for i in range(f):
            T[0][i + 1] = 1
        for i in range(1, d):
            for j in range(1, target + 1):
                for k in range(1, f + 1):
                    if j - k > 0:
                        T[i][j] += T[i - 1][j - k]
                        T[i][j] = T[i][j] % m
        return T[d - 1][target]
