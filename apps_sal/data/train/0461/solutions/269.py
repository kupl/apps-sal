class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        g = defaultdict(list)
        for e,m in enumerate(manager):
            it = informTime[m]
            g[m].append((e,it))
            
        self.mc = 0
        def dfs(node,cost):
            self.mc = max(self.mc, cost)
            
            for child,cc in g[node]:
                dfs(child,cost + cc)
        
        dfs(headID,0)
                
        return self.mc
            
            
            

