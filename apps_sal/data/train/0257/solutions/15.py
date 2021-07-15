from collections import defaultdict, deque


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        stack = deque([start])
        paths = [0 for i in range(n)]
        paths[start] = 1
        
        graph = [{} for i in range(n)]
        for (source, dstn), weight in zip(edges, succProb):
            graph[source][dstn] = graph[dstn][source] = weight
        # seen = set()
        while stack:
            current = stack.popleft()
            for v in graph[current]:
                temp = paths[current] * graph[current][v]
                if temp > paths[v]:
                    stack.append(v)
                    paths[v] = max(temp, paths[v])
        return paths[end] 

