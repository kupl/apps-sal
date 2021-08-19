class Solution:
    def countOrders(self, n: int) -> int:
        # m = m * 2
        res = 1
        for i in range(1, n + 1):
            res = res * self.choose(2 * i, 2)
        return res % int(math.pow(10, 9) + 7)

    def choose(self, n, k):
        if 0 <= k <= n:
            ntok = 1
            ktok = 1
            for t in range(1, min(k, n - k) + 1):
                ntok *= n
                ktok *= t
                n -= 1
            return ntok // ktok
        else:
            return 0
