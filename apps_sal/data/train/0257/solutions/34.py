from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adjlist = defaultdict(list)
        for edge, succ in zip(edges, succProb):
            adjlist[edge[0]].append([edge[1], succ])
            adjlist[edge[1]].append([edge[0], succ])
        cost = [float('-inf')] * n
        hp = [(-1, start)]
        visited = set()
        while hp:
            price, node = heappop(hp)
            price = -price
            if node in visited:
                continue
            for neigh, neighcost in adjlist[node]:
                heappush(hp, (-(price * neighcost), neigh))
            cost[node] = price
            visited.add(node)
        print(cost)
        if cost[end] == float('-inf'):
            return 0
        return cost[end]
