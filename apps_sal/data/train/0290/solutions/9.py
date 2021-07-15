from functools import lru_cache

class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        @lru_cache(None)
        def minCost_r(k,l):
            if l-k <= 1: return 0
            mc = float('inf')
            for c in cuts:
                if c <= k or c >= l: continue
                mc = min(mc, minCost_r(k,c) + minCost_r(c,l) + (l-k))
            return mc if mc != float('inf') else 0
            
        return minCost_r(0,n)

