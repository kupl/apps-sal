#!/usr/bin/env python3
import numpy as np
from itertools import product
import sys
sys.setrecursionlimit(10**6)

n = int(input())

data = np.zeros((10, n), dtype=int)
for i in range(n):
    f = np.array(list(map(int, input().split())))
    data[:, i] = f

# print(data)

p = [list(map(int, input().split())) for i in range(n)]
# print(p)

ans = -10**10

for j, i in enumerate(product([0, 1], repeat=10)):
    if j == 0:
        continue

    indices = [x for x, y in enumerate(i) if y == 1]
    # print(indices)

    data_tmp = data[indices]
    data_tmp = np.sum(data_tmp, axis=0)
    ans_tmp = sum([p[a][b] for a, b in enumerate(data_tmp)])
    ans = max(ans, ans_tmp)
print(ans)
