n = int(input())
coords = [tuple(map(int, input().split())) for i in range(n)]
for (xt, yt, ht) in coords:
    if ht != 0:
        break
(x, y, h) = (-1, -1, -1)
for px in range(101):
    for py in range(101):
        flag = True
        htmp = ht + abs(px - xt) + abs(py - yt)
        dxdy = [(abs(px - x1) + abs(py - y1), htmp - h1) for (x1, y1, h1) in coords]
        dxdy.sort()
        for i in range(n - 1):
            if dxdy[i][0] < dxdy[i + 1][0] and dxdy[i][1] > dxdy[i + 1][1]:
                flag = False
                break
        for (x1, y1, h1) in coords:
            if h1 == 0:
                continue
            if abs(htmp - h1) != abs(px - x1) + abs(py - y1):
                flag = False
                break
        if flag:
            if htmp > h:
                h = htmp
                x = px
                y = py
print(x, y, h)
