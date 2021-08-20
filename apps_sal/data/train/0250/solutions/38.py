class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = [(wage / quality, wage, quality) for (wage, quality) in zip(wage, quality)]
        workers.sort(key=lambda x: x[0])
        heap = []
        quality_sum = 0
        final_cost = float('inf')
        for (ratio, wage, quality) in workers:
            heapq.heappush(heap, -1 * quality)
            quality_sum += quality
            if len(heap) > K:
                q = heapq.heappop(heap)
                quality_sum += q
            if len(heap) == K:
                cost = ratio * quality_sum
                final_cost = min(final_cost, cost)
        return final_cost
