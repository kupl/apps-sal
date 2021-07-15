from collections import deque
from bisect import bisect_left

n = int(input())
a = [int(input()) for _ in range(n)]

dq = deque()
for e in a:
    i = bisect_left(dq, e)
    if i == 0:
        dq.appendleft(e)
    else:
        dq[i-1] = e

ans = len(dq)
print(ans)

