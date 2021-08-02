from math import *
n, k = list(map(int, input().split()))
*m, = list(map(int, input().split()))
d = 0.0
for i in m:
    d += ceil(i / k)
print(ceil(d / 2))
