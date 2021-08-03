class Solution:
    def dfs(self, headId, employee, informTime):
        maxTime = 0

        for e in employee[headId]:
            maxTime = max(maxTime, self.dfs(e, employee, informTime) + informTime[headId])

        return maxTime

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        employee = [[0 for i in range(0)] for j in range(n)]

        for i in range(n):
            if manager[i] != -1:
                employee[manager[i]].append(i)

        return self.dfs(headID, employee, informTime)
