class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        employees_of_manager = [[] for i in range(n)]
        for e, m in enumerate(manager):
            # print(m)
            if m >= 0: 
                employees_of_manager[m].append(e)

        def dfs(i):
            return max([dfs(j) for j in employees_of_manager[i]] or [0]) + informTime[i]
        return dfs(headID)
