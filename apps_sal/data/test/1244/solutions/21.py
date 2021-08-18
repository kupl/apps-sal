import sys
import math

n = int(sys.stdin.readline())
an = [int(x) for x in (sys.stdin.readline()).split()]

d = dict()

for i in an:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

vmax = 0
for i in list(d.keys()):
    if(d[i] > vmax):
        vmax = d[i]

if(vmax <= (n + 1) / 2):
    print("YES")
else:
    print("NO")
