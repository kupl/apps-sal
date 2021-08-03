#!/usr/bin/env python3
from itertools import accumulate
import numpy as np

n, m, q = list(map(int, input().split()))
lr = [list(map(int, input().split())) for _ in range(m)]
pq = [list(map(int, input().split())) for _ in range(q)]

data = [[0] * 500 for i in range(500)]
# data = [[0]*10 for i in range(10)]

for l, r in lr:
    data[l - 1][r - 1] += 1


# for i in range(0, 500):
#     data[i] = list(accumulate(data[i]))

# print(data)
# for p, q in pq:
#     ans = 0
#     if p == 1:
#         for i in range(p-1, q-1+1):
#             ans += data[i][q-1]
#     else:
#         for i in range(p-1, q-1+1):
#             ans += data[i][q-1]-data[i][p-1-1]
#     print(ans)

data = np.array(data)

data = np.cumsum(data, axis=1)
data = np.cumsum(data, axis=0)

# print(data[:10, :10])
for p, q in pq:
    ans = 0
    if p == 1:
        ans = data[q - 1][q - 1]
    else:
        ans = data[q - 1][q - 1] - data[p - 1 - 1][q - 1]
    print(ans)
# for p, q in pq:
#     ans = 0
#     if p == 1:
#         for i in range(p-1, q-1+1):
#             ans += data[i][q-1]
#     else:
#         for i in range(p-1, q-1+1):
#             ans += data[i][q-1]-data[i][p-1-1]
#     print(ans)
