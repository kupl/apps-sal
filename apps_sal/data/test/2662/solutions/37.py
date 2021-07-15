import bisect
from collections import deque

N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

buf = deque()
for a in A:
    i = bisect.bisect_right(buf, a-1)-1
    if i < 0:
        buf.appendleft(a)
    else:
        buf[i] = a
print(len(buf))
