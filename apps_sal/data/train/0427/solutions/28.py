class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10 ** 9 + 7
        # return (2n)! / (2 ^ n)
        res = 1
        for i in range(2 * n, 0, -1):
            res = res * i
            if i & 1:
                res /= 2
                res = res % mod
        return int(res)
