import heapq
from collections import Counter
inf = 10 ** 10
(n, k) = map(int, input().split())
dset = [[] for i in range(n)]
for i in range(n):
    (t, d) = map(int, input().split())
    dset[t - 1].append(d)
for dd in dset:
    if dd:
        dd.sort(reverse=True)
    else:
        dd.append(-inf)
dset.sort(key=lambda x: -x[0])
cur = 0
hq = []
for i in range(k):
    cur += dset[i][0]
    for d in dset[i][1:]:
        heapq.heappush(hq, -d)
for dd in dset[k:]:
    for d in dd:
        heapq.heappush(hq, -d)
ans = cur + k * k
for i in range(k - 1, -1, -1):
    v = dset[i][0]
    if hq:
        w = -heapq.heappop(hq)
    else:
        break
    if v < w:
        cur += w - v
    else:
        heapq.heappush(hq, -w)
    ans = max(ans, cur + i * i)
print(ans)
