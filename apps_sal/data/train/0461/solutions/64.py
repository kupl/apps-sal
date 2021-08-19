from collections import defaultdict


class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        sub = defaultdict(list)
        for (i, s) in enumerate(manager):
            sub[s] += [i]

        def dfs(cur, tot):
            if cur not in sub:
                return tot
            high = max((dfs(employee, tot) + informTime[cur] for employee in sub[cur]))
            return tot + high
        return dfs(headID, 0)
