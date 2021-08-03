from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(n):
            if n not in tree:
                return 0
            return informTime[n] + max(dfs(k) for k in tree[n])

        tree = defaultdict(list)
        for i, v in enumerate(manager):
            if v == -1:
                continue
            tree[v].append(i)
        return dfs(headID)
