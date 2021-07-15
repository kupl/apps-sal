n = int(input())
xyh = []
x0, y0, h0 = None, None, None
for _ in range(n):
    x, y, h = map(int, input().split())
    if h > 0 and x0 is None:
        x0, y0, h0 = x, y, h
    xyh.append([x, y, h])

for cx in range(101):
    for cy in range(101):
        h = h0 + abs(x0 - cx) + abs(y0 - cy)
        done = True
        for xk, yk, hk in xyh:
            h_ = max(h - abs(xk - cx) - abs(yk - cy), 0)
            if h_ != hk:
                done = False
                break
        if done:
            print(f'{cx} {cy} {h}')
