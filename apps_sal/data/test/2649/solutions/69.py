import numpy as np
N = int(input())
x = []
y = []
xy1 = []
xy2 = []
for i in range(N):
    (a, b) = (int(t) for t in input().split())
    x.append(a)
    y.append(b)
    xy1.append(a + b)
    xy2.append(a - b)
max1 = max(xy1) - min(xy1)
max2 = max(xy2) - min(xy2)
print(max((max1, max2)))
