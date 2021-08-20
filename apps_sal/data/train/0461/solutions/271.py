class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subs = [[] for i in range(n)]
        for (i, m) in enumerate(manager):
            if m != -1:
                subs[m].append(i)

        def my_dfs(m):
            if not len(subs[m]):
                return informTime[m]
            return max([my_dfs(s) for s in subs[m]]) + informTime[m]
        return my_dfs(headID)
