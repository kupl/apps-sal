class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [{} for _ in range(n)]
        for u, v in enumerate(manager):
            if v != -1:
                graph[v][u] = informTime[v]
        # print(graph)
        dist = {}
        pq = [(0, headID)]
        dist[headID] = 0
        while pq:
            t, node = heapq.heappop(pq)
            for nei in graph[node]:
                if nei not in dist or graph[node][nei] + t < dist[nei]:
                    dist[nei] = graph[node][nei] + t
                    heapq.heappush(pq, (dist[nei], nei))
        return max(dist.values())
