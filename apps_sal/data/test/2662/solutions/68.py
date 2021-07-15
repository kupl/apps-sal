import bisect
from collections import deque

n = int(input())
#c = []
c = deque([])
for i in range(n):
    a = int(input())
    if i == 0:
        c.append(a)
    else:
        ind = bisect.bisect_left(c,a)
        if ind > 0:
            c[ind-1] = a
        else:
            c.appendleft(a)

print(len(c))
