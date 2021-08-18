n = int(input())

xy = [[-1 for i in range(101)] for j in range(101)]

x = []
y = []
h = []
for i in range(n):
    xx, yy, hh = map(int, input().split())
    x.append(xx)
    y.append(yy)
    h.append(hh)
    if hh > 0:
        x0, y0, h0, = xx, yy, hh

for i in range(101):
    for j in range(101):
        flg = 0
        tmp = h0 + abs(x0 - i) + abs(y0 - j)
        for k in range(n):
            if h[k] != max(tmp - abs(x[k] - i) - abs(y[k] - j), 0):
                flg = 1
                break
        if flg == 0:
            print(i, j, tmp)
            return
