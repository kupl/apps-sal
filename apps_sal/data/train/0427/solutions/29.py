class Solution:

    def countOrders(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        res = 1
        for i in range(2, n + 1):
            res = res * (2 * i - 1) * (2 * i) // 2 % MOD
        return res
