from collections import deque


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        graph = {}

        if len(manager) == 1:
            return 0

        for emp, manager in enumerate(manager):
            if emp == headID:
                continue
            if manager in graph:
                graph[manager].append(emp)
            else:
                graph[manager] = [emp]

        ans = {}

        ans[headID] = 0

        Queue = deque()
        Queue.append(headID)

        maxTime = 0
        while Queue:
            man = Queue.popleft()
            if man not in graph:
                continue
            for emp in graph[man]:
                ans[emp] = ans[man] + informTime[man]
                maxTime = max(maxTime, ans[emp])
                Queue.append(emp)

        return maxTime
