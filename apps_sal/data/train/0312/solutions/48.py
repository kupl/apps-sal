from heapq import *


class Solution:
    def shortestSubarray(self, A, K):
        heap, curS, ans = [(0, -1)], 0, float('inf')
        for i, v in enumerate(A):
            curS += v
            while heap and curS - heap[0][0] >= K:
                ans = min(ans, i - heappop(heap)[1])
            heappush(heap, (curS, i))
        return ans if ans != float('inf') else -1
