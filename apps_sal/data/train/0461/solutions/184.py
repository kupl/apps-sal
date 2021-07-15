class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # adjacency list
        
        adj = [[] for _ in range(n)]
        s = headID
        ans = 0
        visited = [False] * n
        
        for i in range(n):
            if manager[i] == -1:
                continue
            adj[manager[i]].append(i)
            
        def dfs(s, time):
            nonlocal ans
            Leaf = True
            
            for i in adj[s]:
                if not visited[i]:
                    Leaf = False
                    visited[i] = True
                    dfs(i, time + informTime[i])
                    
            if Leaf:
                ans = max(ans, time)
            
            
        dfs(s, informTime[s])
        
        return ans

