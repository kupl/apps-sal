class Solution:
    def knightDialer(self, N: int) -> int:
        M = 10 ** 9 + 7
        d = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [],
             6: [0, 1, 7], 7: [6, 2], 8: [1, 3], 9: [2, 4], 0: [4, 6]}

        out = [1] * 10
        for _ in range(N - 1):
            out1 = [0] * 10
            for j in range(10):
                for k in d[j]:
                    out1[k] += out[j] % M
            out = out1
        return sum(out) % M
