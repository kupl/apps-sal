from heapq import *
from collections import defaultdict


class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for (edge, prob) in zip(edges, succProb):
            (src, dst) = edge
            graph[src].append((dst, prob))
            graph[dst].append((src, prob))
        max_heap = [(-1.0, start, None)]
        while max_heap:
            (probability, node, parent) = heappop(max_heap)
            probability = -probability
            if node == end:
                return probability
            neighbors = graph[node]
            for (neighbor, weight) in neighbors:
                if neighbor != parent:
                    heappush(max_heap, (-weight * probability, neighbor, node))
        return 0
