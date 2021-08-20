class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manager2employee = defaultdict(list)
        for (employee, manager) in enumerate(manager):
            manager2employee[manager].append(employee)

        def dfs(manager):
            if not manager2employee[manager]:
                return 0
            return max([informTime[manager] + dfs(e) for e in manager2employee[manager]])
        return dfs(headID)
