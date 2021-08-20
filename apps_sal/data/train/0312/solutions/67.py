from collections import deque
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


def ksumalt(a, k):
    q = deque()
    q.append((-1, 0))
    cur_sum = 0
    min_len = float('inf')
    for i in range(len(a)):
        cur_sum += a[i]
        while q and cur_sum - q[0][-1] >= k:
            min_len = min(min_len, i - q[0][0])
            q.popleft()
        while q and cur_sum <= q[-1][-1]:
            q.pop()
        q.append((i, cur_sum))
    return -1 if min_len == float('inf') else min_len


class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        return ksumalt(A, K)
