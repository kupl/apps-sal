class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        org = collections.defaultdict(list)
        self.res = 0
        for (i, v) in enumerate(manager):
            org[v].append(i)

        def dfs(manager, time):
            self.res = max(self.res, time)
            for sub in org[manager]:
                dfs(sub, time + informTime[sub])
        dfs(headID, informTime[headID])
        return self.res
