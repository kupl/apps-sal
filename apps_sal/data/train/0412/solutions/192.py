class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        opt = [[0 for i in range(target + 1)] for x in range(d)]
        for i in range(1, target + 1):
            if i <= f:
                opt[0][i] = 1
        for i in range(1, d):
            for j in range(1, target + 1):
                for h in range(1, f + 1):
                    if j - h > -1:
                        opt[i][j] += opt[i - 1][j - h]
        return opt[d - 1][target] % (10 ** 9 + 7)
