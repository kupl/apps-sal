from decimal import Decimal


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = [(Decimal(wage[i] / quality[i]), quality[i]) for i in range(len(wage))]
        heapq.heapify(workers)
        res, unit_price, total_quality, heap = float('inf'), -1.0, 0, []
        while workers:
            u, q = heapq.heappop(workers)
            unit_price = max(u, unit_price)
            heapq.heappush(heap, -q)
            total_quality += q
            # if we already hire K workers, we fire the worker with the highest quality
            if len(heap) > K:
                total_quality += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, total_quality * unit_price)
        return res
