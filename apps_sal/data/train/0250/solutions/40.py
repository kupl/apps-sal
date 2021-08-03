from queue import PriorityQueue


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        ratios = [w / q for w, q in zip(wage, quality)]
        workers = [(r, q, w) for r, q, w in zip(ratios, quality, wage)]
        workers = sorted(workers)

        #heap = []
        pQueue = PriorityQueue()
        min_quality_sum = 0.0
        cost = float('inf')

        for r, q, w in workers:
            pQueue.put(-q)
            min_quality_sum = min_quality_sum + q

            if pQueue.qsize() > K:
                max_quality = pQueue.get()
                min_quality_sum = min_quality_sum + max_quality

            if pQueue.qsize() == K:
                new_cost = r * min_quality_sum
                if new_cost < cost:
                    cost = new_cost

        return cost
