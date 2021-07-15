class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        mod = 10**9 + 7
        m = len(group)
        
        @lru_cache(None)
        def dfs(i, g, p):
            if i == m:
                return int(p <= 0)
            res = 0
            if g - group[i] >= 0:
                res += dfs(i + 1, g - group[i], max(0, p - profit[i]))
            res += dfs(i + 1, g, p)
            return res
        
        return dfs(0, G, P) % mod

