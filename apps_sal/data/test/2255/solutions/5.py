from heapq import heappop, heappush

n, m = list(map(int, input().split()))
a = []
as_ = set()
g = [set() for _ in range(n + 2)]
for _2 in range(m):
    u, v = list(map(int, input().split()))
    g[u].add(v)
    g[v].add(u)
h = [1]
while h:
    u = heappop(h)
    if u not in as_:
        a.append(u)
        as_.add(u)
        for v in g[u]:
            heappush(h, v)
print(*a)

