from collections import defaultdict, deque


class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for (e, m) in enumerate(manager):
            graph[m].append(e)
        res = 0
        queue = deque([(headID, informTime[headID])])
        while queue:
            size = len(queue)
            (employee, time) = queue.popleft()
            res = max(res, time)
            if employee in graph:
                for nei in graph[employee]:
                    queue.append((nei, time + informTime[nei]))
        return res
