class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        n = len(manager)
        graph = collections.defaultdict(list)
        
        for i in range(n):
            graph[manager[i]].append(i)
            
            
        q = [(headID, 0)]
        res = 0
        
        while q:
            node, time = q.pop(0)
            res = max(res, time)
            for nei in graph[node]:
                q.append((nei, time + informTime[node]))
        
        return res
        
        

