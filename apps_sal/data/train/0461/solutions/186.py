class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return informTime[0]
        graph = defaultdict(list)
        
        for i, m in enumerate(manager):
            if m == -1:
                continue
            graph[m].append(i)
        
        #print( graph )
        totalTime = []
        def dfs( node, time=0):
            nonlocal totalTime
            if not graph[node]:
                totalTime.append(time)
            for e in graph[node]:
                dfs(e, time+informTime[e])
            
        
        dfs(headID, time=informTime[headID])
        #print(totalTime)
        return max(totalTime)
