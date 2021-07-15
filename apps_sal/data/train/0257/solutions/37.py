from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adjlist = defaultdict(list)
        for pair, prob in zip(edges, succProb):
            p, c = pair
            adjlist[p].append([c, prob])
            adjlist[c].append([p, prob])
        probability = {i: float('-inf') for i in range(n)}
        hq = [[-1, start]]
        visited = set()
        while hq:
            cost, curr = heappop(hq)
            cost = -cost
            if curr in visited:
                continue
            for child, price in adjlist[curr]:
                heappush(hq, [-(price*cost), child])
            visited.add(curr)
            if probability[curr] < cost:
                probability[curr] = cost
        if probability[end] == float('-inf'):
            return 0
        return probability[end]

