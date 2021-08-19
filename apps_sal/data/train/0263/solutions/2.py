import numpy as np


class Solution:
    def knightDialer(self, n: int) -> int:
        #         d = {1:[6,8],
        #              2:[7,9],
        #              3:[4,8],
        #              4:[3,9,0],
        #              5:[],
        #              6:[1,7,0],
        #              7:[2,6],
        #              8:[1,3],
        #              9:[2,4],
        #              0:[4,6]}
        #         @lru_cache(None)
        #         def dfs(i, n):
        #             if n == 1:
        #                 return 1
        #             else:
        #                 res = 0
        #                 for c in d[i]:
        #                     res += dfs(c, n-1)
        #                 return res % (10**9+7)

        #         return sum(dfs(i, n) for i in range(10)) % (10**9+7)

        mod = 10**9 + 7
        N = n
        if N == 1:
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
        res, N = 1, N - 1
        while N:
            if N % 2:
                res = res * M % mod
            M = M * M % mod
            N //= 2
        return int(np.sum(res)) % mod
