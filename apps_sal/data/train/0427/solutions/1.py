class Solution:
    def countOrders(self, n: int) -> int:

        ans = 1
        MOD = 1000000007
        for i in range(2, n + 1):
            ans *= ((2 * i - 1) * (i - 1) + (2 * i - 1))
            ans %= MOD

        return ans
