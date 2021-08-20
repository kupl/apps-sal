from collections import defaultdict


class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        sub = defaultdict(list)
        for (i, s) in enumerate(manager):
            sub[s] += [i]

        def dfs(cur):
            return max([dfs(employee) for employee in sub[cur]] or [0]) + informTime[cur]
        return dfs(headID)
