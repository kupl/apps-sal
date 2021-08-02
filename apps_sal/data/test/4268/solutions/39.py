import numpy as np
from itertools import combinations
n, b = map(int, input().split())
xlist = [list(map(int, input().split())) for _ in range(n)]

xnumpy = np.array(xlist)
ans = 0
for y, z in combinations(xnumpy, 2):
    distance = ((y - z)**2).sum()
    for i in range((40**2) * 10):
        if distance == i * i:
            ans += 1
print(ans)
