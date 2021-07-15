from heapq import heappush, heappop


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        stack = [(-1, start)]
        paths = [0 for i in range(n)]
        paths[start] = 1
        
        graph = [{} for i in range(n)]
        for (source, dstn), weight in zip(edges, succProb):
            graph[source][dstn] = graph[dstn][source] = weight
        while stack:
            _, current = heappop(stack)
            for v in graph[current]:
                temp = paths[current] * graph[current][v]
                if temp > paths[v]:
                    heappush(stack, (-temp, v))
                    paths[v] = max(temp, paths[v])
        return paths[end] 

