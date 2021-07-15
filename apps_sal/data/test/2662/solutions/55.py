from collections import deque
import bisect

N = int(input())

A = [int(input()) for i in range(N)]

q = deque([A[0]])

for a in A[1:]:
    idx = bisect.bisect_left(q, a)
    if idx == 0:
        q.appendleft(a)
    else:
        q[idx-1] = a

print(len(q))
