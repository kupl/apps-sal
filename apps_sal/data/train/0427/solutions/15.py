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

        @lru_cache(None)
        def factorial(x):
            fact = 1
            for i in range(1, x + 1):
                fact *= i
            return fact
        mod = 10**9 + 7

        @lru_cache(None)
        def ways(pickOptions, deliverOptions):
            nonlocal mod
            ans = 0
            if pickOptions > 0 and deliverOptions > 0:
                ans += ways(pickOptions - 1, deliverOptions + 1) * pickOptions
                ans += ways(pickOptions, deliverOptions - 1) * deliverOptions
            elif pickOptions > 0 and deliverOptions == 0:
                ans += ways(pickOptions - 1, deliverOptions + 1) * pickOptions
            elif deliverOptions > 0 and pickOptions == 0:
                ans += factorial(deliverOptions)
            return ans % mod
        return ways(n, 0)
