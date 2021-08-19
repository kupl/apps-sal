class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10 ** 9 + 7
        N = n
        R = len(rollMax)
        T = [0] * (N + 1)
        D = [[0] * R for _ in range(N + 1)]
        T[0] = 1
        T[1] = R
        D[1] = [1] * R
        for i in range(2, N + 1):
            for j in range(R):
                lim = max(i - rollMax[j], 0)
                for k in range(i - 1, lim - 1, -1):
                    D[i][j] += T[k] - D[k][j]
            T[i] = sum(D[i])
        return sum(D[-1]) % mod
