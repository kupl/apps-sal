from heapq import heappop, heappush


class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        hh = [[efficiency[ii], speed[ii]] for ii in range(n)]
        hh.sort(reverse=True)
        heap = []
        cursum = 0
        cureff = hh[0][0]
        ans = 0
        for (ih, [e, s]) in enumerate(hh):
            heappush(heap, (s, ih))
            (tops, topind) = heap[0]
            cursum = cursum + s
            if len(heap) > k:
                heappop(heap)
                cursum = cursum - hh[topind][1]
            cureff = e
            ans = max(ans, cureff * cursum)
        return ans % (10 ** 9 + 7)
