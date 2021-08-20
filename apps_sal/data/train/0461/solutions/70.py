class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = {}
        for i in range(n):
            if i == headID:
                continue
            graph[manager[i]] = graph.get(manager[i], []) + [i]
        self.output = 0

        def dfs(v, time):
            if v not in graph:
                self.output = max(self.output, time)
                return
            for w in graph[v]:
                dfs(w, time + informTime[v])
        dfs(headID, 0)
        return self.output
