import heapq
from math import log2


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        AdjList = [set() for _ in range(n)]
        for (u, v), prob in zip(edges, succProb):
            AdjList[u].add((-log2(prob), v))
            AdjList[v].add((-log2(prob), u))
        dist = [float('inf')] * n
        dist[start] = 0
        heap = [(0, start)]
        explored = set()
        while heap:
            d, curr = heapq.heappop(heap)
            explored.add(curr)
            for (val, node) in AdjList[curr]:
                if node not in explored:
                    if dist[curr] + val < dist[node]:
                        dist[node] = dist[curr] + val
                        heapq.heappush(heap, (dist[node], node))
        return 2 ** (-dist[end])
