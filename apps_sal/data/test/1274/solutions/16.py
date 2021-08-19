import heapq
(n, m) = map(int, input().split())
ab = [[] for _ in range(m + 1)]
for i in range(n):
    t = [int(inp) for inp in input().split()]
    if t[0] <= m:
        ab[t[0]].append(-t[1])
ans = 0
h = ab[1]
heapq.heapify(h)
for i in range(1, m + 1):
    if len(h) > 0:
        ans += heapq.heappop(h)
    if i != m:
        for t in ab[i + 1]:
            heapq.heappush(h, t)
print(-ans)
