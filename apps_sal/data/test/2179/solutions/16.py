import heapq

n, m = list(map(int, input().split()))
g = [[] for _ in range(n + 1)]
for i in range(1, m + 1):
    u, v, w = list(map(int, input().split()))
    g[u].append((i, v, w))
    g[v].append((i, u, w))
src = int(input())

pq = [(0, 0, src, -1)]
mk = [0] * (n + 1)
t = []
s = 0
while pq:
    d, w, u, e = heapq.heappop(pq)
    if mk[u]:
        continue
    mk[u] = 1
    s += w
    t.append(e)
    for e, v, w in g[u]:
        if not mk[v]:
            heapq.heappush(pq, (d + w, w, v, e))

print(s)
print(*t[1:])

