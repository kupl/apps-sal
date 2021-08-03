class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = [[] for i in range(n)]

        for index, m in enumerate(manager):
            if m >= 0:
                children[m].append(index)

        def dfs(ID):
            if children[ID]:
                return max(dfs(j) for j in children[ID]) + informTime[ID]

            return informTime[ID]

        return dfs(headID)
