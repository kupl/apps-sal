from collections import deque


class Solution:
    def shortestSubarray(self, A, K):
        acc = [0]
        for v in A:
            acc.append(acc[-1] + v)
        ans, monoq = float('inf'), deque()
        for size, curS in enumerate(acc):
            while monoq and curS < acc[monoq[-1]]:
                monoq.pop()
            while monoq and curS - acc[monoq[0]] >= K:
                ans = min(ans, size - monoq.popleft())
            monoq.append(size)
        return ans if ans != float('inf') else -1
