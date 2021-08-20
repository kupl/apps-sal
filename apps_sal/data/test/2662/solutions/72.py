from collections import deque
from bisect import bisect_left
n = int(input())
a = [int(input()) for i in range(n)]
d = deque()
for i in range(n):
    b = bisect_left(d, a[i])
    if b == 0:
        d.appendleft(a[i])
    else:
        d[b - 1] = a[i]
print(len(d))
