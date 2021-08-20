class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        (managerToReports, ms) = (defaultdict(set), set([headID]))
        for (i, m) in enumerate(manager):
            managerToReports[m].add(i)

        def dfs(parent):
            return max([dfs(report) for report in managerToReports[parent]] or [0]) + informTime[parent]
        return dfs(headID)
