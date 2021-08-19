from typing import *
from heapq import heappop, heappush


class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        N = len(quality)
        heap_quality = []
        workers = [i for i in range(N)]
        workers = sorted(workers, key=lambda x: wage[x] / quality[x])
        sum_quality = 0
        for i in range(K):
            heappush(heap_quality, -quality[workers[i]])
            sum_quality += quality[workers[i]]
        ans = sum_quality * (wage[workers[K - 1]] / quality[workers[K - 1]])
        for i in range(K, N):
            heappush(heap_quality, -quality[workers[i]])
            sum_quality += quality[workers[i]]
            sum_quality += heappop(heap_quality)
            ans = min(ans, sum_quality * (wage[workers[i]] / quality[workers[i]]))
        return ans
