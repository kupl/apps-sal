from heapq import heapify, heappop, heappush
n, m = map(int, input().split())
g = [[]for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append((c, b, i))
    g[b].append((c, a, i))
no_used = [1] * m


def dks(t0):
    todo = [[0, t0, -1]]
    heapify(todo)
    seen = [0] * n
    while todo:
        d, t, i = heappop(todo)
        if seen[t] and seen[t] < d: continue
        seen[t] = d
        if i > -1: no_used[i] = 0
        l = g[t]
        for d_, t_, i_ in l:
            heappush(todo, [d + d_, t_, i_])


for i in range(n):
    dks(i)
print(sum(no_used))
