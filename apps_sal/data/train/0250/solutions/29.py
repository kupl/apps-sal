class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = sorted([(w / q, q, w) for (w, q) in zip(wage, quality)])
        print(workers)
        result = math.inf
        qualitySum = 0
        maxheap = []
        for (r, q, _) in workers:
            heapq.heappush(maxheap, -q)
            qualitySum += q
            if len(maxheap) > K:
                qualitySum += heapq.heappop(maxheap)
            if len(maxheap) == K:
                print((qualitySum * r, r, qualitySum))
                result = min(result, qualitySum * r)
        return result
