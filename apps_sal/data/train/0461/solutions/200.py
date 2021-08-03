class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        graph = {i: [] for i in range(n)}
        for child, parent in enumerate(manager):
            if parent == -1:
                continue
            graph[parent].append(child)

        time = 0
        pq = [(0, headID)]
        maxtime = 0
        while pq:
            curtime, curm = heapq.heappop(pq)
            for nxt in graph[curm]:
                heapq.heappush(pq, (curtime + informTime[curm], nxt))
            maxtime = curtime
        return maxtime
