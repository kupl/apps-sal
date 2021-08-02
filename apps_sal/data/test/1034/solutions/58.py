# D - Cake 123

import heapq
import itertools

x, y, z, k = map(int, input().split())

A = list(int(a) for a in input().split())
B = list(int(b) for b in input().split())
C = list(int(c) for c in input().split())

hq = []
for i, j in itertools.product(A, B):
    heapq.heappush(hq, (i + j) * -1)

AB = []
while len(hq) > 0 and len(AB) <= k:
    AB.append(heapq.heappop(hq) * -1)

hq = []
for i, j in itertools.product(AB, C):
    heapq.heappush(hq, (i + j) * -1)

for _ in range(k):
    print(heapq.heappop(hq) * -1)
