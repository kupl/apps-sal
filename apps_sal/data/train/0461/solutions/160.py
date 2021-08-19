class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Step1: build the graph
        adjList = collections.defaultdict(list)
        for i, (u, v) in enumerate(zip(manager, informTime)):
            adjList[u].append((i, v))
        # Step2: dfs with stack
        stack = adjList[-1]
        res = 0
        while stack:
            u, v = stack.pop()
            res = max(res, v)
            for nu, nv in adjList[u]:
                stack.append((nu, v + nv))
        return res
