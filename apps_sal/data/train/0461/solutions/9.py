from collections import deque


class Solution:

    def build_graph(self, n, manager):
        graph = {i: [] for i in range(n)}
        for (i, m) in enumerate(manager):
            if m == -1:
                continue
            graph[m].append(i)
        return graph

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = self.build_graph(n, manager)
        if not graph[headID]:
            return 0
        queue = deque([(headID, informTime[headID])])
        t = 0
        informed = set()
        while queue:
            (boss, time) = queue.popleft()
            t = max(t, time)
            for employee in graph[boss]:
                if employee in informed:
                    continue
                queue.append((employee, time + informTime[employee]))
                informed.add(employee)
        return t
