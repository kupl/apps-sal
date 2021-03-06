import sys
import math
n = int(sys.stdin.readline())
d = []
vmin = 1000000001
vmax = 0
for i in range(n):
    (l, r) = [int(x) for x in sys.stdin.readline().split()]
    d.append((i + 1, (l, r)))
    if l < vmin:
        vmin = l
    if r > vmax:
        vmax = r
d.sort(key=lambda x: x[1][0])
k = -1
for i in d:
    if i[1][0] <= vmin:
        if i[1][1] >= vmax:
            k = i[0]
    else:
        break
print(k)
