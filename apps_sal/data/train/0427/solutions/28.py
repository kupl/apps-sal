class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10 ** 9 + 7
        res = 1
        for i in range(2 * n, 0, -1):
            res = res * i
            if i & 1:
                res /= 2
                res = res % mod
        return int(res)
