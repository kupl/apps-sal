class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        results = [[0 for _ in range(7)] for _ in range(n + 1)]
        results[0][6] = 1

        for i in range(1, n + 1):
            for j in range(6):
                suma = 0
                for roll_max in range(min(rollMax[j], i)):
                    suma += results[i - 1 - roll_max][6] - results[i - 1 - roll_max][j]
                results[i][j] = suma
            results[i][6] = sum(results[i])

        return results[n][6] % (10**9 + 7)
