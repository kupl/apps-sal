import heapq


class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], probs: List[float], s: int, t: int) -> float:
        graph = {u: {} for u in range(n)}
        for ((u, v), prob) in zip(edges, probs):
            graph[u][v] = prob
            graph[v][u] = prob
        frontier = [(-1, s)]
        seen = set()
        while len(frontier) != 0:
            (neg_path_prob, u) = heapq.heappop(frontier)
            if u == t:
                return -neg_path_prob
            seen.add(u)
            for (v, edge_prob) in graph[u].items():
                if v not in seen:
                    heapq.heappush(frontier, (neg_path_prob * edge_prob, v))
        return 0
