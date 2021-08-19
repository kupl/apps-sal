import numpy as np


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        # print(workers)
        res = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:
            # print(\"*****r: \", r, \"q: \", q)
            heapq.heappush(heap, -q)
            qsum += q
            # print(\"sum:\", qsum)
            # print(heap)
            if len(heap) > K:
                # print(\"popping from heap\")
                qsum += heapq.heappop(heap)
                # print(\"qsum: \", qsum)
            if len(heap) == K:
                res = min(res, qsum * r)
                # print(\"min: \", res)
        return res
