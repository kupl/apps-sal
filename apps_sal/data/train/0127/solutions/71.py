import functools


class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        n = len(profit)

        @functools.lru_cache(None)
        def dp(g, p, i):
            if i == n or g == 0:
                if p == 0:
                    return 1
                return 0

            ans = dp(g, p, i + 1)
            if g - group[i] >= 0:
                ans += dp(g - group[i], max(0, p - profit[i]), i + 1)

            return ans % (10**9 + 7)

        return dp(G, P, 0) % (10**9 + 7)
