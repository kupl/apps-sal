import math
from statistics import mean
e1, e2 = list(map(int, input().split()))
h = []
for i in range(e1):
    h.append(list(map(int, input().split())))
r = []
count = 0
for i in range(e1):
    if h[i][1] <= e2:
        r.append(h[i][0])

if len(r) > 0:
    print((min(r)))
else:
    print("TLE")
