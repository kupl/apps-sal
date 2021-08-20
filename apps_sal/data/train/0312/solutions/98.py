from heapq import *


class Solution:

    def shortestSubarray(self, A, K):
        (N, acc) = (len(A), [0])
        for v in A:
            acc.append(acc[-1] + v)
        (ans, monoq) = (float('inf'), deque())
        for (size, curS) in enumerate(acc):
            while monoq and curS <= acc[monoq[-1]]:
                monoq.pop()
            while monoq and curS - acc[monoq[0]] >= K:
                ans = min(ans, size - monoq.popleft())
            monoq.append(size)
        return ans if ans != float('inf') else -1


class Solution:

    def shortestSubarray(self, A, K):
        (heap, curS, ans) = ([(0, -1)], 0, float('inf'))
        for (i, v) in enumerate(A):
            curS += v
            while heap and curS - heap[0][0] >= K:
                ans = min(ans, i - heappop(heap)[1])
            heappush(heap, (curS, i))
        return ans if ans != float('inf') else -1
