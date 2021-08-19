import numpy as np
import heapq as hq
N = int(input())
F = np.array([[int(x) for x in input().split()] for _ in range(N)])
P = np.array([[int(x) for x in input().split()] for _ in range(N)])
Profit = []
for i in range(1, 2 ** 10):
    Open = np.array([int(x) for x in format(i, '010b')]).T
    c = np.dot(F, Open)
    hq.heappush(Profit, -sum((P[i, c[i]] for i in range(N))))
print(-Profit[0])
