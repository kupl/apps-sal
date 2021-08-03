from heapq import heappush, heappop


def kmin(a, k):
    cur_sum = 0
    h = [(0, -1)]
    min_ = float('inf')
    for i in range(0, len(a)):
        cur_sum += a[i]
        while h and h[0][0] <= cur_sum - k:
            min_ = min(min_, i - h[0][1])
            heappop(h)
        heappush(h, (cur_sum, i))
    return min_ if min_ != float('inf') else -1


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        return kmin(A, K)
