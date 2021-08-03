class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(node, curTime):
            nonlocal totalTime
            visited.add(node)
            totalTime = max(curTime, totalTime)
            for nextNode in graph[node]:
                if nextNode not in visited:
                    dfs(nextNode, curTime + informTime[node])
        graph = defaultdict(set)
        totalTime = 0
        visited = set()
        for u, v in enumerate(manager):
            graph[u].add(v)
            graph[v].add(u)
        visited.add(-1)
        dfs(headID, 0)
        return totalTime
