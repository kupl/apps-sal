class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MODE = 1e9 + 7
        f = [[0 for _ in range(7)] for _ in range(n + 1)]
        f[0][6] = 1
        for i in range(1, n + 1):
            for j in range(6):
                for k in range(1, rollMax[j] + 1):
                    if i - k < 0:
                        break
                    f[i][j] = (f[i][j] + (f[i - k][6] - f[i - k][j]) % MODE) % MODE
                f[i][6] = (f[i][j] + f[i][6]) % MODE
        return int(f[n][-1])
