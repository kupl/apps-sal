class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        ratios = [(w / q, i) for (i, (q, w)) in enumerate(zip(quality, wage))]
        ratios.sort()
        heap = []
        sumq = 0
        ans = math.inf
        for (ratio, i) in ratios:
            sumq += quality[i]
            heapq.heappush(heap, -quality[i])
            if len(heap) > K:
                q = heapq.heappop(heap)
                sumq += q
            if len(heap) == K:
                ans = min(ans, sumq * ratio)
        return ans
