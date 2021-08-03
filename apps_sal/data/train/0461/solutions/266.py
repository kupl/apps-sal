from collections import deque


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        graph = {}

        for emp, manager in enumerate(manager):
            if manager in graph:
                graph[manager].append(emp)
            else:
                graph[manager] = [emp]

        ans = {}

        ans[headID] = 0

        Queue = deque()
        Queue.append(headID)
        maxele = 0
        while Queue:
            cid = Queue.popleft()
            if cid not in graph:
                continue
            for emp in graph[cid]:
                ans[emp] = ans[cid] + informTime[cid]
                maxele = max(maxele, ans[emp])
                Queue.append(emp)

        return maxele
