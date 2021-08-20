from heapq import *


class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = []
        for i in range(len(quality)):
            workers.append([wage[i] / quality[i], wage[i], quality[i]])
        workers = sorted(workers, key=lambda x: [x[0], x[2], x[1]])
        cost = math.inf
        maxHeap = []
        tot = 0
        for (r, w, q) in workers:
            heappush(maxHeap, -q)
            tot += q
            if len(maxHeap) > K:
                tot += heappop(maxHeap)
            if len(maxHeap) == K:
                cost = min(cost, r * tot)
        return float(cost)
