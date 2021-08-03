from functools import lru_cache


class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        @lru_cache(None)
        def sack(g, i, p):
            if i == len(profit) or g == 0:
                return p >= P
            ans = 0
            if group[i] <= g:
                ans = sack(g - group[i], i + 1, min(P, p + profit[i]))
            return ans + sack(g, i + 1, p)
        return sack(G, 0, 0) % (10**9 + 7)
