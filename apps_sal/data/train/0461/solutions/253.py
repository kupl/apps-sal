from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def dfs_visit(u):
            v = manager[u]
            if manager[v] != -1:
                dfs_visit(v)
            informTime[u] += informTime[v]
            manager[u] = -1
            return informTime[u]

        res = 0
        for u in range(n):
            if manager[u] != -1:
                res = max(res, dfs_visit(u))
        return res
