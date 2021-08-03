class Solution:

    def knightDialer(self, n: int) -> int:
        import numpy as np
        mod = 10**9 + 7
        if n == 1:
            return 10
        M = np.matrix([[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                       [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]])
        res = np.matrix([[1] * 10])
        n -= 1
        while n:
            if n % 2 != 0:
                res = res * M % mod
                n -= 1
            else:
                M = M * M % mod
                n /= 2
        return int(np.sum(res)) % mod
