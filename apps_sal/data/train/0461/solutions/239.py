class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = {}
        res = 0
        for (e, m) in enumerate(manager):
            graph[m] = graph.get(m, []) + [e]
        stack = [(headID, 0)]
        while stack:
            (curr, time) = stack.pop()
            res = max(res, time)
            if curr in graph:
                for e in graph[curr]:
                    stack.append((e, time + informTime[curr]))
        return res
