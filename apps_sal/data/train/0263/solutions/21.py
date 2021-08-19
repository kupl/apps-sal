class Solution:

    def knightDialer1(self, N: int) -> int:
        (m, n) = (4, 3)
        M = 10 ** 9 + 7

        def dp(i, j, k):
            if k == 0:
                return 1
            out = 0
            for (x, y) in [(i + 2, j + 1), (i - 2, j + 1), (i + 2, j - 1), (i - 2, j - 1), (i + 1, j + 2), (i + 1, j - 2), (i - 1, j + 2), (i - 1, j - 2)]:
                if 0 <= x < m and 0 <= y < n and (x != 3 or y not in [0, 2]):
                    out += dp(x, y, k - 1)
            return out
        out = 0
        for i in range(m):
            for j in range(n):
                if i != m - 1 or j not in [0, 2]:
                    out += dp(i, j, N - 1)
        return out

    def knightDialer(self, N: int) -> int:
        M = 10 ** 9 + 7
        d = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [0, 1, 7], 7: [6, 2], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        out = [1] * 10
        for i in range(N - 1):
            out1 = [0] * 10
            for j in range(10):
                for k in d[j]:
                    out1[k] += out[j] % M
            out = out1
        return sum(out) % M
