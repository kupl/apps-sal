import heapq
from collections import defaultdict
x, y, z, K = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))[::-1]
b = sorted(list(map(int, input().split())))[::-1]
c = sorted(list(map(int, input().split())))[::-1]

used = defaultdict(bool)
pq = [(-(a[0] + b[0] + c[0]), 0, 0, 0)]
used[(0, 0, 0)] = True
heapq.heapify(pq)

for _ in range(K):
    d, i, j, k = heapq.heappop(pq)
    print((-d))
    if i + 1 < x and not used[(i + 1, j, k)]:
        heapq.heappush(pq, (-(a[i + 1] + b[j] + c[k]), i + 1, j, k))
        used[(i + 1, j, k)] = True
    if j + 1 < y and not used[(i, j + 1, k)]:
        heapq.heappush(pq, (-(a[i] + b[j + 1] + c[k]), i, j + 1, k))
        used[(i, j + 1, k)] = True
    if k + 1 < z and not used[(i, j, k + 1)]:
        heapq.heappush(pq, (-(a[i] + b[j] + c[k + 1]), i, j, k + 1))
        used[(i, j, k + 1)] = True

