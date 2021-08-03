class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        table = [[0 for _ in range(len(rollMax) + 1)] for _ in range(n + 1)]
        table[0][len(rollMax)] = 1

        for j in range(len(rollMax)):
            table[1][j] = 1

        table[1][len(rollMax)] = 6

        for i in range(2, n + 1):
            for j in range(len(rollMax)):
                for k in range(1, rollMax[j] + 1):
                    if i - k < 0:
                        break
                    table[i][j] += table[i - k][len(rollMax)] - table[i - k][j]
            table[i][len(rollMax)] = sum(table[i])
        return table[-1][-1] % (10**9 + 7)
