class Solution:

    def countOrders(self, n: int) -> int:
        res = 1
        for i in range(1, n + 1):
            x = (i - 1) * 2 + 1
            possibilities = x * (x - 1) // 2 + x
            res = res * possibilities % (1000000000 + 7)
        return res
