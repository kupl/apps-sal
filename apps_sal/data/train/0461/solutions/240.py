class Solution:

    def dfs(self, node, visited, graph, minute, informTime):
        visited[node] = minute
        for neighbour in graph[node]:
            self.dfs(neighbour, visited, graph, minute + informTime[node], informTime)

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []
        for i in range(len(manager)):
            if manager[i] != -1:
                graph[manager[i]] += [i]
        visited = [-1 for i in range(n)]
        visited[headID] = 0
        self.dfs(headID, visited, graph, 0, informTime)
        return max(visited)
