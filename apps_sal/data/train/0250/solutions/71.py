class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        from fractions import Fraction
        workers = sorted(((Fraction(w, q), q, w) for (q, w) in zip(quality, wage)))
        ans = float('inf')
        heap = []
        heapSum = 0
        for (ration, q, w) in workers:
            heapq.heappush(heap, -q)
            heapSum += q
            if len(heap) > K:
                heapSum += heapq.heappop(heap)
            if len(heap) == K:
                ans = min(ans, ration * heapSum)
        return float(ans)
