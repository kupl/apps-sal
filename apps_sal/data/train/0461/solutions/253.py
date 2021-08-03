from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Top down approach is ok
        # Bottom up approach: COPIED
        # Idea is: Given any employee, recursively (going up the chain of command) compute its time to
        # reach the head. Then, for a different employee, check if its managers computed value is set
        # via the dfs call. If it is, use it directly, else make the dfs call as before, and so on for each employee.

        # Lee's solution uses manager as a way to mark if the dfs call for an employee has been made.
        # Let's do it assuming we should not modify manager => maintain a separate array
        # This is basically the usual DFS on the directed graph as provided
        # With each DFS visit, we add the informTime of an employee's manager to the informTime of the employee
        # So informTime will now tell you the time to reach the head from the employee
        # To avoid using visited[], we'd need to modify manager

        # def dfs_visit(u):
        # visited[u] = True
        # v = manager[u]
        # if v == -1:
        #     return 0
        # else:
        #     if not visited[v]:
        #         _ = dfs_visit(v)
        #     informTime[u] += informTime[v]
        #     return informTime[u]

        # Without visited, modifying manager
        def dfs_visit(u):
            v = manager[u]
            if manager[v] != -1:
                dfs_visit(v)
            informTime[u] += informTime[v]
            manager[u] = -1
            return informTime[u]

        #visited = [False]*n
        res = 0
        for u in range(n):
            # if not visited[u]:
            if manager[u] != -1:
                res = max(res, dfs_visit(u))
        return res
