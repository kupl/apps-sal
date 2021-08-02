import heapq
from operator import itemgetter

n, k = list(map(int, input().split()))
sushi = [tuple(map(int, input().split())) for _ in range(n)]

sushi.sort(key=itemgetter(1), reverse=True)
que = []
kind = set()
res = 0
for t, d in sushi[:k]:
    if t in kind:
        heapq.heappush(que, d)
    else:
        kind.add(t)
    res += d
res += len(kind)**2

val = res
for t, d in sushi[k:]:
    if not que:
        break
    if t in kind:
        continue
    val += -heapq.heappop(que) + d + len(kind) * 2 + 1
    kind.add(t)
    res = max(res, val)

print(res)
