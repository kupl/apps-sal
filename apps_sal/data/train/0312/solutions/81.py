import heapq


class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        q = [(0, -1)]
        cum = 0
        res = float('inf')
        for (i, x) in enumerate(A):
            cum += x
            while q and cum - q[0][0] >= K:
                res = min(res, i - heapq.heappop(q)[1])
            heapq.heappush(q, (cum, i))
        return res if res < float('inf') else -1
