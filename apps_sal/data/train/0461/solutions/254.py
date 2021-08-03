class Solution:
    over_all_max_time = 0

    def DFS(self, edgeList, max_time, headID, informTime):
        if len(edgeList[headID]) == 0:
            Solution.over_all_max_time = max(Solution.over_all_max_time, max_time)
            return

        for emp in edgeList[headID]:
            max_time += informTime[headID]
            self.DFS(edgeList, max_time, emp, informTime)
            max_time -= informTime[headID]

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        Solution.over_all_max_time = 0
        edgeList = {i: [] for i in range(n)}
        for cur_emp in range(n):
            cur_emp_manager = manager[cur_emp]
            if cur_emp_manager != -1:
                edgeList[cur_emp_manager].append(cur_emp)
        self.DFS(edgeList, 0, headID, informTime)
        return Solution.over_all_max_time
