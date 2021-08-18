class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        g = collections.defaultdict(list)
        for i, v in enumerate(manager):
            g[v].append(i)

        def dfs(i):
            return informTime[i] if not g[i] else max([informTime[i] + dfs(c) for c in g[i]])

        return dfs(headID)
