from collections import defaultdict as ddict
from collections import deque


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        maxProb = ddict(float)

        graph = ddict(dict)

        for [a, b], sucprob in zip(edges, succProb):
            graph[a][b] = sucprob if b not in graph[a] else max(sucprob, graph[a][b])
            graph[b][a] = sucprob if a not in graph[b] else max(sucprob, graph[b][a])

        print(graph)

        que = deque()
        que.append((start, 1))
        while que:
            node, prob = que.popleft()
            maxProb[node] = max(maxProb[node], prob)

            for child in graph[node]:
                if prob * graph[node][child] > maxProb[child]:
                    que.append((child, prob * graph[node][child]))

        return maxProb[end]
