class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        dp = [0.0 for _ in range(start)] + [1.0] + [0.0 for _ in range(start + 1, n)]
        # dp[i] is the prob of getting node i from node start

        graph = defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))

        # dijkstra's algorithm
        heap = [(-1.0, start)]

        while heap:
            p, cur = heapq.heappop(heap)
            if cur == end:
                return -p
            for child, prob in graph[cur]:
                if dp[cur] * prob > dp[child]:
                    dp[child] = dp[cur] * prob
                    heapq.heappush(heap, (-dp[child], child))
        return 0
