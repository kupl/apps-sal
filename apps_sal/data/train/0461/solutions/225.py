class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        for i in range(len(manager)):
            if manager[i] == -1:
                continue
            graph[manager[i]].append(i)
        return self.dfs(headID, graph, informTime)

    def dfs(self, head, graph, informTime):
        time = 0
        for employee in graph[head]:
            time = max(time, self.dfs(employee, graph, informTime))
        return informTime[head] + time
