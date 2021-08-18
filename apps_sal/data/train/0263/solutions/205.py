class Solution:
    def knightDialer(self, n: int) -> int:
        d = {1: [6, 8], 2: [7, 9], 3: [8, 4], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        f = [[0] * 10 for i in range(2)]
        f[1 & 1] = [1] * 10
        for i in range(2, n + 1):
            f[i & 1] = [0] * 10
            for j in range(10):
                for v in d[j]:
                    f[i & 1][v] += f[(i - 1) & 1][j] % (10**9 + 7)
        return sum(f[n & 1]) % (10**9 + 7)
