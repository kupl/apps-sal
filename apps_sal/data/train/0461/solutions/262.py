class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        managerMap = defaultdict(list)

        for i, v in enumerate(manager):
            managerMap[v].append(i)

        def dfs(mgr):
            return max([dfs(emp) for emp in managerMap[mgr]] or [0]) + informTime[mgr]

        return dfs(headID)
