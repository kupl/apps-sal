class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        # top-down approach
        # key: (i, t, c) -> cost for paint i house left t group with c color
        
        cache = {}
        
        # dfs search
        def dfs(i, t, c):
            key = (i, t, c)
            
            # boundary condition
            # 1. we paint all house and no target left
            # 2. t must in  0 < t < m - i  
            if i == len(houses) or t < 0 or m - i < t:
                return 0 if i == len(houses) and t == 0 else float('inf')
            
            if key not in cache:
                print(key)
                if houses[i] == 0: 
                    # compte 
                    cache[key] = min(dfs(i + 1, t - int(nc != c), nc) + cost[i][nc - 1]
                                   for nc in range(1, n + 1)) 
                else:
                    # if already paint no extra cost add
                    cache[key] = dfs(i + 1, t - int(c != houses[i]), houses[i])
                    
                
            return cache[key]
        
        result = dfs(0, target, 0)
        print(cache.keys())
        
        return result if result < float('inf') else -1
