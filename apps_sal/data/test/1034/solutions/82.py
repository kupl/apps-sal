import heapq
(x, y, z, k) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
q = []
s = set()
heapq.heappush(q, (-a[0] - b[0] - c[0], 0, 0, 0))
for i in range(k):
    (ans, ai, bi, ci) = heapq.heappop(q)
    print(-ans)
    if ai < x - 1 and (ai + 1, bi, ci) not in s:
        heapq.heappush(q, (-a[ai + 1] - b[bi] - c[ci], ai + 1, bi, ci))
        s.add((ai + 1, bi, ci))
    if bi < y - 1 and (ai, bi + 1, ci) not in s:
        heapq.heappush(q, (-a[ai] - b[bi + 1] - c[ci], ai, bi + 1, ci))
        s.add((ai, bi + 1, ci))
    if ci < z - 1 and (ai, bi, ci + 1) not in s:
        heapq.heappush(q, (-a[ai] - b[bi] - c[ci + 1], ai, bi, ci + 1))
        s.add((ai, bi, ci + 1))
