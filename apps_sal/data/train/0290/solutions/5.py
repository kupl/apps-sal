from functools import lru_cache
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        
        @lru_cache(maxsize=None)
        def dfs(l, r):
            m = 0xffffffff
            for c in cuts:
                if l < c < r:
                    m = min(m, dfs(l, c) + dfs(c, r))
            return 0 if m == 0xffffffff else m + r - l

        return dfs(0, n)
