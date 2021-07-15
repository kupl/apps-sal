class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def dfs(node, currTime):
            nonlocal ans
            
            if node not in graph:
                ans = max(ans, currTime)
            
            for nei in graph[node]:
                dfs(nei, currTime + informTime[node])
        
        graph = defaultdict(list)
        for u, v in enumerate(manager):
            graph[v].append(u)
 
        ans = 0
        dfs(headID, 0)
        return ans

