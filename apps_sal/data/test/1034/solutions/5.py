import heapq
(x, y, z, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
hq = [[-a[0] - b[0] - c[0], 0, 0, 0]]
heapq.heapify(hq)
visited = {(0, 0, 0)}
for i in range(k):
    (ii, ia, ib, ic) = heapq.heappop(hq)
    print(-ii)
    na = min(ia + 1, x - 1)
    nb = min(ib + 1, y - 1)
    nc = min(ic + 1, z - 1)
    if not (na, ib, ic) in visited:
        heapq.heappush(hq, [-a[na] - b[ib] - c[ic], na, ib, ic])
        visited.add((na, ib, ic))
    if not (ia, nb, ic) in visited:
        heapq.heappush(hq, [-a[ia] - b[nb] - c[ic], ia, nb, ic])
        visited.add((ia, nb, ic))
    if not (ia, ib, nc) in visited:
        heapq.heappush(hq, [-a[ia] - b[ib] - c[nc], ia, ib, nc])
        visited.add((ia, ib, nc))
