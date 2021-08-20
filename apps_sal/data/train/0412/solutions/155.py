class Solution:

    def numRollsToTarget(self, dice: int, faces: int, target: int) -> int:
        table = [[0 for _ in range(target + 1)] for _ in range(dice + 1)]
        table[0][0] = 1
        mod = 10 ** 9 + 7
        for d in range(1, dice + 1):
            for i in range(1, target + 1):
                for f in range(1, min(i + 1, faces + 1)):
                    table[d][i] = (table[d][i] + table[d - 1][i - f]) % mod
        return table[-1][-1]
