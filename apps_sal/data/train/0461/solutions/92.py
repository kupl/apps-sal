class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def dfs(node):
            if manager[node] != -1:
                informTime[node] += dfs(manager[node])
                manager[node] = -1
            return informTime[node]
        return max(dfs(i) for i in range(n))
