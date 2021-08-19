class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        F = [[0 for i in range(6)] for i in range(n + 1)]
        sumF = [0 for i in range(n + 1)]
        for i in range(6):
            F[1][i] = 1
        sumF[1] = 6
        MOD = 10 ** 9 + 7
        for i in range(2, n + 1):
            for j in range(6):
                for p in range(1, rollMax[j] + 1):
                    if i == p:
                        F[i][j] = (F[i][j] + 1) % MOD
                        continue
                    elif i > p:
                        F[i][j] = (F[i][j] + sumF[i - p] - F[i - p][j]) % MOD
                sumF[i] += F[i][j]
        res = 0
        for i in range(6):
            res = (res + F[n][i]) % MOD
        return round(res)
