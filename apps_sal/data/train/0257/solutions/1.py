class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(dict)
        for edge, prob in zip(edges, succProb):
            s, t = edge
            graph[s][t] = prob
            graph[t][s] = prob

        heap = [(-1, start)]
        prob = [0] * n
        prob[start] = 1
        visited = [False] * n

        while heap:
            curr_prob, node = heapq.heappop(heap)
            if visited[node]:
                continue
            if node == end:
                return prob[end]
            curr_prob *= -1
            visited[node] = True
            for neighbor in graph[node]:
                if visited[neighbor]:
                    continue
                p = curr_prob * graph[node][neighbor]
                if p > prob[neighbor]:
                    prob[neighbor] = p
                    heapq.heappush(heap, (-p, neighbor))

        return prob[end]
