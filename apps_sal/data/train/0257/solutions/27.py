class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)
        for (s, e), prob in zip(edges, succProb):
            graph[s].append((e, prob))
            graph[e].append((s, prob))

        visited = [0] * n

        prio = [(-1, start)]
        while prio:
            prob, vertex = heapq.heappop(prio)

            if prob > visited[vertex]:
                continue
            visited[vertex] = prob

            if vertex == end:
                return -prob

            for neighbor, cost in graph[vertex]:
                if prob * cost < visited[neighbor]:
                    visited[neighbor] = prob * cost
                    heapq.heappush(prio, (prob * cost, neighbor))

        return 0
