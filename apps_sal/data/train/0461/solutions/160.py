class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjList = collections.defaultdict(list)
        for i, (u, v) in enumerate(zip(manager, informTime)):
            adjList[u].append((i, v))
        stack = adjList[-1]
        res = 0
        while stack:
            u, v = stack.pop()
            res = max(res, v)
            for nu, nv in adjList[u]:
                stack.append((nu, v + nv))
        return res
