import numpy as np
import heapq as hq
N = int(input())
F = np.array([[int(x) for x in input().split()] for _ in range(N)])
P = np.array([[int(x) for x in input().split()] for _ in range(N)])

Profit = []
for i in range(1, 2**10):
    Open = np.array([int(x) for x in format(i, '010b')])
    prf = 0
    for f, p in zip(F, P):
        cnt = np.dot(Open, f)
        prf += p[cnt]
    hq.heappush(Profit, -prf)
print((-Profit[0]))
