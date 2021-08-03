class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9 + 7
        dc = {(x, 1): 1 for x in range(10)}

        for i in range(1, n):
            dc[(0, i + 1)] = (dc[(4, i)] + dc[(6, i)]) % mod
            dc[(1, i + 1)] = (dc[(6, i)] + dc[(8, i)]) % mod
            dc[(2, i + 1)] = (dc[(7, i)] + dc[(9, i)]) % mod
            dc[(3, i + 1)] = (dc[(4, i)] + dc[(8, i)]) % mod
            dc[(4, i + 1)] = (dc[(0, i)] + dc[(3, i)] + dc[(9, i)]) % mod
            dc[(5, i + 1)] = 0
            dc[(6, i + 1)] = (dc[(0, i)] + dc[(1, i)] + dc[(7, i)]) % mod
            dc[(7, i + 1)] = (dc[(2, i)] + dc[(6, i)]) % mod
            dc[(8, i + 1)] = (dc[(1, i)] + dc[(3, i)]) % mod
            dc[(9, i + 1)] = (dc[(2, i)] + dc[(4, i)]) % mod

        res = 0
        for j in range(10):
            res = (res + dc[(j, n)]) % mod
        return res
