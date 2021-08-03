import sys
n = int(input())
l, d, r, u = map(int, input().split())
l1 = d1 = r1 = u1 = 0
rects = [(l, d, r, u)]
may = (0, 0)
for i in range(n - 1):
    a, b, c, e = map(int, input().split())
    rects.append((a, b, c, e))

for i in range(n):
    a, b, c, e = rects[i]
    if a > r:
        may = (r1, i)
        break
    if b > u:
        may = (u1, i)
        break
    if c < l:
        may = (l1, i)
        break
    if e < d:
        may = (d1, i)
        break
    if a > l:
        l = a
        l1 = i
    if b > d:
        d = b
        d1 = i
    if c < r:
        r = c
        r1 = i
    if e < u:
        u = e
        u1 = i
for x in may:
    ind = max(1 - x, 0)
    l, d, r, u = rects[ind]
    for i in range(n):
        if i != x:
            l = max(l, rects[i][0])
            d = max(d, rects[i][1])
            r = min(r, rects[i][2])
            u = min(u, rects[i][3])
    if l <= r and d <= u:
        print(l, d)
        return
