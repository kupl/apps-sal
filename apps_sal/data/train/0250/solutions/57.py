from heapq import heappush, heappop


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        from fractions import Fraction
        cap_wage = sorted((Fraction(w, q), q, w) for q, w in zip(quality, wage))
        cap_wage = sorted([(w / c, c, w) for c, w in zip(quality, wage)])
        heap = []
        re = float('inf')
        val = 0
        for ratio, c, w in cap_wage:
            heappush(heap, -c)
            val += c
            if len(heap) > K:
                val += heappop(heap)
            if len(heap) == K:
                re = min(re, val * ratio)
        return float(re)
