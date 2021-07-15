from functools import lru_cache
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        @lru_cache(None)
        def dfs(i,prev,k):
            if i>=m:
                return 0 - int(k!=0)
                
            if k<0:
                return -1
                
            if houses[i]!=0:
                return dfs(i+1, houses[i], k - int(prev!=houses[i]))
            
            else:
                temp = float('inf')
                for c in range(1,n+1):
                    c_cost = cost[i][c-1]
                    other = dfs(i+1,c, k-int(prev!=c))
                    
                    if other>=0:
                        temp = min(temp, c_cost+other)
                if temp == float('inf'):
                    return -1
                return temp
        return dfs(0,0,target)
            
            

