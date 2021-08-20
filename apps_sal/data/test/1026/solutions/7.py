from math import *
import sys
from queue import *
n = int(input())
a = list(map(int, input().split()))
d = {}
mx = 0
for i in range(n):
    d[a[i] - i] = d.get(a[i] - i, 0) + a[i]
    mx = max(mx, d[a[i] - i])
print(mx)
