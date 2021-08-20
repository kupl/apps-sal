class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        table = [[0] * (target + 1) for i in range(d + 1)]
        for j in range(1, min(f + 1, target + 1)):
            table[1][j] = 1
        for i in range(2, d + 1):
            for j in range(1, target + 1):
                for k in range(1, min(f + 1, j)):
                    table[i][j] += table[i - 1][j - k]
        return table[-1][-1] % 1000000007
