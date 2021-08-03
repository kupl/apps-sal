class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        managerToReports, ms = defaultdict(set), set([headID])
        for i, m in enumerate(manager):
            managerToReports[m].add(i)
        self.result = 0

        def dfs(parent, consumedTime):
            if not managerToReports[parent]:
                self.result = max(self.result, consumedTime)
            [dfs(report, consumedTime + informTime[parent]) for report in managerToReports[parent]]
        dfs(headID, 0)
        return self.result
