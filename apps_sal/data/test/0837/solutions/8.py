import heapq
(n, x, y) = list(map(int, input().split()))
h = []
d = {}
heapq.heappush(h, (0, n))
r = -1
while r == -1:
    (xh, nh) = heapq.heappop(h)
    if nh not in d:
        d[nh] = xh
        if nh == 1:
            r = xh + x
        elif nh * x < y:
            r = xh + nh * x
        else:
            if nh - 1 not in d:
                heapq.heappush(h, (xh + x, nh - 1))
            if nh & 1 == 0 and nh // 2 not in d and (y < nh // 2 * x):
                heapq.heappush(h, (xh + y, nh // 2))
            if nh + 1 not in d:
                heapq.heappush(h, (xh + x, nh + 1))
print(r)
