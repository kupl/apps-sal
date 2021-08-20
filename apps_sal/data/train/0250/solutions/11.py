class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = sorted(([float(w) / q, q] for (w, q) in zip(wage, quality)))
        ans = float('inf')
        heap = []
        heapSum = 0
        for (ratio, q) in workers:
            heapq.heappush(heap, -q)
            heapSum += q
            if len(heap) > K:
                heapSum += heapq.heappop(heap)
            if len(heap) == K:
                ans = min(ans, ratio * heapSum)
        return float(ans)
