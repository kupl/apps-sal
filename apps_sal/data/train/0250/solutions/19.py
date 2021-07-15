class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        wq = sorted([(a / b, b) for (a, b) in zip(wage, quality)])
        res = float('inf')
        heap = []
        qSum = 0
        for avg, q in wq:
            qSum += q
            heapq.heappush(heap, -q)
            if len(heap) > K: qSum += heapq.heappop(heap)
            if len(heap) == K: res = min(res, avg * qSum)
        return res
