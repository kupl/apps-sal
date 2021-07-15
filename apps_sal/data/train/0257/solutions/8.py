from heapq import heappop, heappush
from sys import maxsize as inf
from collections import defaultdict as dic

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = dic(dict)

        for [u, v], w in zip(edges,succProb):
            graph[u][v] = w
            graph[v][u] = w

        dist = { i : 0 for i in range(n)}
        dist[start] = 1
        visited = set()
        max_prob = [(-1*1,start)]
        while len(max_prob):
            cur_prob, cur_node = heappop(max_prob)
            if cur_node in visited:
                continue
            visited.add(cur_node)
            for nei in graph[cur_node]:
                if nei in visited:
                    continue
                if dist[nei] < graph[cur_node][nei] * (-1*cur_prob):
                    dist[nei] = graph[cur_node][nei] * (-1*cur_prob)
                    heappush(max_prob, ((-1*dist[nei]),nei) )
                    
            if cur_node == end:
                break

        return(dist[end])

