class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        n = len(group)
        
        @lru_cache(None)
        def dfs(i, g, p):         
            if g == 0:
                return 1 if p <= 0 else 0
            
            if i == n:
                return 1 if p <= 0 else 0
            
            ans = dfs(i+1, g, p)
            if group[i] <= g:
                ans += dfs(i+1, g-group[i], max(p-profit[i], 0))
                
            return ans % (10 ** 9 + 7)
        
        return dfs(0, G, P) % (10 ** 9 + 7)
