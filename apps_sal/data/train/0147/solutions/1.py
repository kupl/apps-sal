from heapq import *


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        ids = [i for i in range(n)]
        ids = sorted(ids, key=lambda x: -efficiency[x])
        max_perf, heap = 0, []
        sum = 0
        for i in ids:
            if len(heap) == k:
                sum -= heappop(heap)
            heappush(heap, speed[i])
            sum += speed[i]
            max_perf = max(max_perf, sum * efficiency[i])

        return max_perf % (10 ** 9 + 7)
