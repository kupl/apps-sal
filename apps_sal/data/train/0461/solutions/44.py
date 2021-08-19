class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def dfs(emp_id):

            # no subordinates
            if not graph[emp_id]:
                return 0
            max_path = float('-inf')
            for subordinate, time in graph[emp_id]:
                max_path = max(max_path, time + dfs(subordinate))
            return max_path

        # create graph from boss -> [(emp,informtime)]
        graph = collections.defaultdict(list)
        for emp, boss in enumerate(manager):
            graph[boss].append((emp, informTime[boss]))
        del graph[-1]
        return dfs(headID)
