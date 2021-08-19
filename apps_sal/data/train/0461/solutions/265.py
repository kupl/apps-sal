class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        minutes = 0
        g = defaultdict(list)
        for i in range(n):
            g[manager[i]].append(i)

        def dfs(eid, elapsed):
            nonlocal minutes
            if not g[eid]:
                minutes = max(minutes, elapsed)
            for sub in g[eid]:
                dfs(sub, elapsed + informTime[eid])
        dfs(headID, 0)
        return minutes
