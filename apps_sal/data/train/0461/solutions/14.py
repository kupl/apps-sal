from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(employee):
            if manager[employee] != -1:
                informTime[employee] += dfs(manager[employee])
                manager[employee] = -1
            return informTime[employee]
        return max(list(map(dfs, list(range(n)))))
