class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        dp = [0.0 for _ in range(start)] + [1.0] + [0.0 for _ in range(n)]
        graph = defaultdict(list)  # undirected
        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))

        queue = [(-1.0, start)]  # tuple[0] is current point, tuple[1] is prob of getting cur from start

        while queue:
            for _ in range(len(queue)):
                p, cur = heapq.heappop(queue)
                if cur == end:
                    return -p
                for child, prob in graph[cur]:
                    if dp[cur] * prob > dp[child]:
                        dp[child] = dp[cur] * prob
                        heapq.heappush(queue, (-dp[child], child))

        return 0
