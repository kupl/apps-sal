from collections import deque
from bisect import bisect_left
N = int(input())
A = [int(input()) for _ in range(N)]
que = deque()
for i in range(N):
    k = bisect_left(que, A[i])
    if k == 0:
        que.appendleft(A[i])
    else:
        que[k - 1] = A[i]

print(len(que))
