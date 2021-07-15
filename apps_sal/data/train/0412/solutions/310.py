class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        @lru_cache(None)
        def dfs(rsum,d):
            
            if d==0 and rsum==0:
                return 1
            
            elif rsum==0 or d==0:
                return 0
            
            res=0
            for i in range(1,f+1):
                if rsum-i>=0:
                    res+=dfs(rsum-i,d-1)
                    
            return res
        
        
        return dfs(target,d)%(10**9+7)

