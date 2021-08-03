class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = sorted([(w / q, q) for q, w in zip(quality, wage)])
        heap = []
        sumq = 0
        res = float('inf')

        for r, q in workers:
            heapq.heappush(heap, -q)
            sumq += q

            if len(heap) > K:
                sumq += heapq.heappop(heap)

            if len(heap) == K:
                res = min(res, sumq * r)

        return res
