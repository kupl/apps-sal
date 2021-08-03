from heapq import heappop, heappush
n, m, s = map(int, input().split())
g = [[]for i in range(n)]
x = 0
for i in range(m):
    u, v, a, b = map(int, input().split())
    g[u - 1].append([v - 1, a, b])
    g[v - 1].append([u - 1, a, b])
    x = max(x, a)
for i in range(n):
    c, d = map(int, input().split())
    g[i].append([i, -c, d])
x *= (n - 1)
t = [[2**64 for i in range(x + 1)]for i in range(n)]
q = []
heappush(q, (0, 0, s))
while q:
    a, b, c = heappop(q)
    for i, j, h in g[b]:
        if c >= j and a + h < t[i][min(x, c - j)]:
            t[i][min(x, c - j)] = a + h
            heappush(q, (a + h, i, c - j))
for i in range(1, n):
    print(min(t[i]))
