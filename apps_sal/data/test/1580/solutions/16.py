import heapq
import sys
sys.setrecursionlimit(10**8)
n, m = map(int, input().split())
c = [0] * n
g = [[] for i in range(n)]
revealed = [False] * n
rn = 0

for i in range(m):
    x, y, z = map(int, input().split())
    x -= 1; y -= 1
    c[x] += 1
    c[y] += 1
    g[y].append(x)
    g[x].append(y)

hq = [(c[i], i) for i in range(n)]
heapq.heapify(hq)


def dfs(src):
    nonlocal rn
    rn += 1
    revealed[src] = True
    for nxt in g[src]:
        if not revealed[nxt]:
            dfs(nxt)


ans = 0
while rn < n:
    _, now = heapq.heappop(hq)
    if revealed[now]: continue
    revealed[now] = True
    ans += 1
    dfs(now)
print(ans)
