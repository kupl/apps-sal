import sys
import math
n = int(sys.stdin.readline())
pn = [int(x) for x in sys.stdin.readline().split()]
vmax = 0
rmax = 0
ind = 0
for i in range(n):
    if pn[i] > vmax:
        rmax = vmax
        vmax = pn[i]
        ind = i + 1
    elif pn[i] > rmax:
        rmax = pn[i]
print(ind, rmax)
