def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())
import heapq

n, m = mi()
g = [[] for i in range(n + 1)]
for i in range(m):
    u, v = mi()
    g[u].append(v)
    g[v].append(u)

vis = [0] * (n + 1)
vis[1] = 1
pq = [1]
ans = []
while pq:
    u = heapq.heappop(pq)
    ans.append(u)
    for v in g[u]:
        if not vis[v]:
            heapq.heappush(pq, v)
            vis[v] = 1

print(*ans)

