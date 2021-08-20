import sys
from heapq import heappush, heappop
lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\r\n'))
(n, m) = lines[0].split()
n = int(n)
m = int(m)
a = []
for i in range(n):
    (x, y) = lines[i + 1].split()
    x = int(x)
    y = int(y) * -1
    a.append((x, y))
a.sort()
a.append((0, 0))
h = []
cur = 0
summ = 0
for i in range(1, m + 1):
    while cur < n and a[cur][0] <= i:
        heappush(h, a[cur][1])
        cur += 1
    if len(h) > 0:
        summ += heappop(h) * -1
print(summ)
