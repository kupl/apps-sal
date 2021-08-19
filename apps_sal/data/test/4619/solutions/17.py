(w, h, n) = map(int, input().split())
xya = [list(map(int, input().split())) for _ in range(n)]
(x, y, a) = zip(*xya)
(xl, xr, yb, yt) = (0, w, 0, h)
for i in range(n):
    if a[i] == 1:
        xl = max(xl, x[i])
    elif a[i] == 2:
        xr = min(xr, x[i])
    elif a[i] == 3:
        yb = max(yb, y[i])
    else:
        yt = min(yt, y[i])
print((xr - xl) * (yt - yb) * (xr > xl and yt > yb))
