class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        dist = [-math.inf for _ in range(n)]
        dist[start] = 1
        max_heap = [(1, start)]
        graph = collections.defaultdict(dict)

        for (u, v), w in zip(edges, succProb):
            graph[u][v] = w
            graph[v][u] = w

        while max_heap:
            prob, node = heapq.heappop(max_heap)
            prob = abs(prob)
            if node == end:
                return prob
            for adj in graph[node]:
                next_prob = graph[node][adj]
                next_prob *= prob
                if dist[adj] < next_prob:
                    dist[adj] = next_prob
                    heapq.heappush(max_heap, (-next_prob, adj))
        return 0.0
