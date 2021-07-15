class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        @lru_cache(maxsize=None)
        def dfs(c,l,d):
            nonlocal n
            nonlocal rollMax
            
            
            if rollMax[l] < d:
                return 0
            
            if c == n:
                return 1
            
            sm = 0
            
            for i in range(0,6):
                sm += dfs(c+1,i,1+d*(i==l))
                    
            
            return sm
        
        return dfs(0,-1,0)%(10**9 +7)
