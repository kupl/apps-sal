from collections import deque
import bisect

N = int(input())
A = [int(input()) for _ in range(N)]

Q = deque([A[0]])
for a in A[1:]:
    if a <= Q[0]:
        Q.appendleft(a)
    else:
        idx = bisect.bisect_left(Q,a)
        Q[idx-1] = a

print(len(Q))
