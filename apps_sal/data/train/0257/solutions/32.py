from collections import deque
from heapq import heappush, heappop

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        for (u, v), wt in zip(edges, succProb):
            graph[u].append((v, wt))
            graph[v].append((u, wt))
        
        probabilities = [0 for _ in range(n)]
        probabilities[start] = 1
        h = [(-probabilities[start], start)]
        visited = set()
        while h:
            curr_prob, curr_node = heappop(h)
            curr_prob *= -1
            visited.add(curr_node)
            for v, wt in graph[curr_node]:
                if v not in visited:
                    if probabilities[curr_node] * wt > probabilities[v]:
                        probabilities[v] = probabilities[curr_node] * wt
                        heappush(h, (-probabilities[v], v))
        return probabilities[end]
            
        
        

