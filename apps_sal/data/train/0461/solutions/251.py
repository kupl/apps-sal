class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = [[] for _ in range(n)]
        for i, x in enumerate(manager):
            if x >= 0:
                children[x].append(i)

        def dfs(p):
            return max([dfs(x) for x in children[p]] or [0]) + informTime[p]

        return dfs(headID)
