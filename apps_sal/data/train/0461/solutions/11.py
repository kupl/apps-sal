class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        subs = [[] for i in range(n)]
        for i, m in enumerate(manager):
            if m != -1:
                subs[m].append(i)

        def my_dfs(root):

            if subs[root] is None:
                return informTime[root]

            return max([my_dfs(s) for s in subs[root]] or [0]) + informTime[root]

        return my_dfs(headID)
