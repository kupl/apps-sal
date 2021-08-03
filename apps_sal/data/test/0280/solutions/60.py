# n<=8
from bisect import bisect_left
from itertools import permutations
n, m = map(int, input().split())
*w, = map(int, input().split())

llvv = [tuple(map(int, input().split())) for _ in range(m)]
ww = max(w)
vv = min(x[1] for x in llvv)
if ww > vv:
    print(-1)
    return

llvv.sort(key=lambda x: x[1])

v = [0] + [vi for li, vi in llvv]
l = [0] + [li for li, vi in llvv]
for i in range(m):
    l[i + 1] = max(l[i], l[i + 1])

INF = 10**15

ans = INF
for p in permutations(range(n)):
    dist = [0 for _ in range(n)]
    for i in range(n):
        tmp = w[p[i]]
        for j in range(i + 1, n):
            tmp += w[p[j]]
            t = bisect_left(v, tmp)
            if t:
                dist[j] = max(dist[j], dist[i] + l[t - 1])
            else:
                dist[j] = max(dist[j], dist[i])
    ans = min(ans, dist[-1])
print(ans)
