class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        def method1():
            graph = collections.defaultdict(set)
            for i, pair in enumerate(edges):
                u, v = pair
                graph[u].add((v, succProb[i]))
                graph[v].add((u, succProb[i]))

            seen = {0: 0}
            queue = [(start, -1)]
            ans = float('-inf')
            while queue:
                node, p = heapq.heappop(queue)
                p = -p
                if node == end:
                    ans = max(ans, p)
                for nei, dw in graph[node]:
                    if (nei not in seen or seen[nei] < p * dw) and p * dw > ans:
                        seen[nei] = p * dw
                        heapq.heappush(queue, (nei, -p * dw))

            return ans if ans != float('-inf') else 0

        # return method1()

        def method2():
            AdjList = [set() for _ in range(n)]

            for (u, v), p in zip(edges, succProb):
                AdjList[u].add((v, log2(1 / p)))
                AdjList[v].add((u, log2(1 / p)))

            dist = [float('inf') for _ in range(n)]
            dist[start] = 0
            h = [(0, start)]
            while h:
                d, u = heappop(h)
                if d == dist[u]:
                    for (v, p) in AdjList[u]:
                        if dist[u] + p < dist[v]:
                            dist[v] = dist[u] + p
                            heappush(h, (dist[v], v))
            return 1 / (2 ** dist[end])
        return method2()
