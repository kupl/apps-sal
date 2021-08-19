from collections import defaultdict


class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n <= 1:
            return 0
        d = defaultdict(list)
        for i in range(len(manager)):
            d[manager[i]].append(i)
        self.ans = 0
        self.dfs(headID, d, 0, informTime)
        return self.ans

    def dfs(self, node, d, totalTime, informTime):
        self.ans = max(self.ans, totalTime)
        for sub in d[node]:
            self.dfs(sub, d, totalTime + informTime[node], informTime)
