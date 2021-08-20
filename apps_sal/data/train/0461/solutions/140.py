class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.employee = collections.defaultdict(list)
        self.time = 0
        self.infromTime = informTime
        for (i, m) in enumerate(manager):
            self.employee[m].append(i)
        self.dfs(headID, informTime[headID])
        return self.time

    def dfs(self, rootID, time):
        self.time = max(time, self.time)
        for employee in self.employee[rootID]:
            self.dfs(employee, time + self.infromTime[employee])
