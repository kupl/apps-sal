class Solution:
    def countOrders(self, n: int) -> int:

        pickup = n
        delivery = 0

        def factorial(x):
            fact = 1
            for i in range(1, x + 1):
                fact *= i
            return fact
        mod = 10**9 + 7

        @lru_cache(None)
        def ways(pick, deliver):
            nonlocal mod
            ans = 0
            if pick > 0 and deliver > 0:
                ans += ways(pick - 1, deliver + 1) * pick
                ans += ways(pick, deliver - 1) * deliver
            elif pick > 0 and deliver == 0:
                ans += ways(pick - 1, deliver + 1) * pick
            elif deliver > 0 and pick == 0:
                ans += factorial(deliver)
            return ans % mod
        return ways(n, 0)
