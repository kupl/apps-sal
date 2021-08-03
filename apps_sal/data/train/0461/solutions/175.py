class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subord = [[] for i in range(n)]
        for i, m in enumerate(manager):
            if m >= 0:
                subord[m].append(i)

        return self.dfs(headID, subord, informTime)

    def dfs(self, i, subord, informTime):
        return max([self.dfs(e, subord, informTime) for e in subord[i]] or [0]) + informTime[i]
