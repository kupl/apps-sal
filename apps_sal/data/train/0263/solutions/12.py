import numpy as np


class Solution:

    def knightDialer(self, N: int) -> int:
        mod = 10 ** 9 + 7
        moves = np.matrix([[0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]])
        res = np.matrix([[1] * 10])
        N -= 1
        while N:
            if N % 2 != 0:
                res = res * moves % mod
                N -= 1
            else:
                moves = moves * moves % mod
                N //= 2
        return int(np.sum(res)) % mod
