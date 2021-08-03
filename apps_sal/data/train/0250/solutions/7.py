class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        extra_worker_heap = list()
        for i in range(len(quality)):
            heappush(extra_worker_heap, (wage[i] / quality[i], quality[i]))

        hired_worker_heap = list()
        hired_quality = 0
        wage_to_quality = 0
        min_cost = 1e10
        while extra_worker_heap:
            cur_wage_to_quality, worker_quality = heappop(extra_worker_heap)
            hired_quality += worker_quality
            heappush(hired_worker_heap, -worker_quality)
            while len(hired_worker_heap) > K:
                hired_quality += heappop(hired_worker_heap)
            if len(hired_worker_heap) == K:
                min_cost = min(min_cost, hired_quality * cur_wage_to_quality)
        return min_cost
