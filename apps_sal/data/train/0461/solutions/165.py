from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        '''

        if not manager:
            return 0

        graph = defaultdict(list)
        for v in range(n):
            graph[manager[v]].append(v)

        def dfs(node):
            if node not in graph:
                return informTime[node]
            else:
                return  informTime[node]+max(map(lambda n: dfs(n), graph[node]))

        return dfs(headID)
        '''

        if not manager:
            return 0
        g = collections.defaultdict(list)
        for e, m in enumerate(manager):
            g[m].append(e)

        def dfs(u):
            if u not in g:
                return 0
            return informTime[u] + max(dfs(v) for v in g[u])

        return dfs(headID)
