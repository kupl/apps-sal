class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = [[] for i in range(n)]
        for (index, m) in enumerate(manager):
            if m >= 0:
                children[m].append(index)

        def dfs(ID):
            return max([dfs(j) for j in children[ID]] or [0]) + informTime[ID]
        return dfs(headID)
