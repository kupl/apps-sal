from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, managers: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for subord, manager in enumerate(managers):
            graph[manager].append(subord)

        return self.dfs(headID, graph, informTime)

    def dfs(self, node, graph, informTime):
        longest = 0
        for child in graph[node]:
            longest = max(longest, self.dfs(child, graph, informTime))
        return longest + informTime[node]

    def numOfMinutes(self, n: int, headID: int, managers: List[int], informTime: List[int]) -> int:
        # if I want to go from top-to-bottom I will always have to search for the employees of a given manager via linear search
        # -> not efficient, if I do that I explicitly build up a graph or adjacency matrix (manager -> employees)
        # -> O(n) time + O(n) space

        # can I go bottom-up too to avoid the space cost? -> I think would work if I can from all employees with time 0 (else too expensive)
        manager_to_employees = [[] for _ in managers]
        for employee, manager in enumerate(managers):
            if manager == -1:
                continue
            manager_to_employees[manager].append(employee)
        max_time = [0]
        self.dfs(headID, informTime, manager_to_employees, 0, max_time)
        return max_time[0]

    def dfs(self, ID, informTime, manager_to_employees, curr_time, max_time):
        if not manager_to_employees[ID]:
            max_time[0] = max(max_time[0], curr_time)
        for employee in manager_to_employees[ID]:
            self.dfs(employee, informTime, manager_to_employees, curr_time + informTime[ID], max_time)
