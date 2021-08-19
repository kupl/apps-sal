from collections import defaultdict, deque


class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        stack = deque([start])
        paths = {i: 0 for i in range(n)}
        paths[start] = 1
        graph = defaultdict(dict)
        for ((source, dstn), weight) in zip(edges, succProb):
            graph[source][dstn] = weight
            graph[dstn][source] = weight
        while stack:
            current = stack.popleft()
            for v in graph[current]:
                if paths[current] * graph[current][v] > paths[v]:
                    stack.append(v)
                    paths[v] = max(paths[current] * graph[current][v], paths[v])
        return paths[end]
