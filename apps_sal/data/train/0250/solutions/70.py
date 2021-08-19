from fractions import Fraction
from heapq import *


class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = sorted(((Fraction(w, q), q, w) for (q, w) in zip(quality, wage)))
        result = float('inf')
        maxheap = []
        current_sum = 0
        for (ratio, q, w) in workers:
            heappush(maxheap, -q)
            current_sum += q
            if len(maxheap) > K:
                current_sum += heappop(maxheap)
            if len(maxheap) == K:
                result = min(result, ratio * current_sum)
        return float(result)
