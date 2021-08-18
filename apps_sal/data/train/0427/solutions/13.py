class Solution:
    def countOrders(self, n: int) -> int:

        mod = 10**9 + 7
        facts = [1]
        for i in range(1, n + 1):
            facts.append(facts[-1] * i)

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
                ans += facts[deliverOptions]
            return ans % mod
        return ways(n, 0)
