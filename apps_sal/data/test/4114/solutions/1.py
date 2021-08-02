N = int(input())
xs, ys, hs = [], [], []
for _ in range(N):
    x, y, h = map(int, input().split())
    if h != 0:
        xx, yy, hh = x, y, h
    xs.append(x)
    ys.append(y)
    hs.append(h)
for cx in range(101):
    for cy in range(101):
        H = hh + abs(xx - cx) + abs(yy - cy)
        if all([hs[i] == max(0, H - abs(cx - xs[i]) - abs(cy - ys[i])) for i in range(N)]):
            print(cx, cy, H)
            return
