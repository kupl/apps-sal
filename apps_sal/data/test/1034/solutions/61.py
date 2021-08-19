import heapq
(x, y, z, k) = list(map(int, input().split()))
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
al = []
hq = []
heapq.heappush(hq, (-(a[0] + b[0] + c[0]), 0, 0, 0))
for i in range(k):
    (hqi, ai, bi, ci) = heapq.heappop(hq)
    print(-hqi)
    if ai + 1 < x and (not (ai + 1, bi, ci) in al):
        heapq.heappush(hq, (-(a[ai + 1] + b[bi] + c[ci]), ai + 1, bi, ci))
        al.append((ai + 1, bi, ci))
    if bi + 1 < y and (not (ai, bi + 1, ci) in al):
        heapq.heappush(hq, (-(a[ai] + b[bi + 1] + c[ci]), ai, bi + 1, ci))
        al.append((ai, bi + 1, ci))
    if ci + 1 < z and (not (ai, bi, ci + 1) in al):
        heapq.heappush(hq, (-(a[ai] + b[bi] + c[ci + 1]), ai, bi, ci + 1))
        al.append((ai, bi, ci + 1))
