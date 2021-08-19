class Solution:
    def countOrders(self, n: int) -> int:
        # 9:41
        # we just want to make sure delivery i happens before pick up i
        # we can save lot of recursive calls by using maths

        #         n*[(n-1),1]
        #                    n-2

        #         p,d
        #         n,0

        #         p=n
        #         d=0

        #         p=n-1
        #         d=1

        #         p=n-2   or p=n-1
        #                d=0
        #         d=2.

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
