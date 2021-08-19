import sys
from heapq import *
(n, k) = map(int, input().split())
N = int(200000.0 + 2)
ll = [[] for _ in range(N)]
rr = [[] for _ in range(N)]
vis = [0] * N
for i in range(n):
    (l, r) = map(int, sys.stdin.readline().split())
    ll[l].append((-r, i + 1))
    rr[r].append(i + 1)
q = []
ans = []
size = 0
for i in range(1, N):
    for j in ll[i]:
        heappush(q, j)
        size += 1
    while size > k:
        cur = heappop(q)
        vis[cur[1]] = 1
        ans.append(cur[1])
        size -= 1
    for j in rr[i]:
        if not vis[j]:
            vis[j] = 1
            size -= 1
print(len(ans))
print(*ans)
