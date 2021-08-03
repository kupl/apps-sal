class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        for i in range(n):
            graph[manager[i]].append(i)

        def dfs(manager, curr_time):
            self.max_time = max(self.max_time, curr_time)
            for subordinate in graph[manager]:
                dfs(subordinate, curr_time + informTime[manager])

        self.max_time = 0
        dfs(headID, 0)
        return self.max_time
