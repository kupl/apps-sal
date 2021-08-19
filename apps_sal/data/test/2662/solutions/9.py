from collections import deque
from bisect import bisect_left
n = int(input())
d = deque()
for i in range(n):
    a = int(input())
    b = bisect_left(d, a)
    if b == 0:
        d.appendleft(a)
    else:
        d[b - 1] = a
print(len(d))
