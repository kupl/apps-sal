from collections import defaultdict


class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if not manager:
            return 0
        graph = defaultdict(list)
        for v in range(n):
            graph[manager[v]].append(v)

        def dfs(node):
            if node not in graph:
                return informTime[node]
            else:
                return informTime[node] + max([dfs(n) for n in graph[node]])
        return dfs(headID)
