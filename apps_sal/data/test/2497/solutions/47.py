N = int(input())
x1, x2, y1, y2 = {}, {}, {}, {}
INF = 10 ** 10

for i in range(N):
    x, y, d = input().split()
    x, y = int(x) * 2, int(y) * 2

    def update_x(v, x):
        if v not in x1:
            x1[v] = x2[v] = x
        else:
            x1[v] = min(x1[v], x)
            x2[v] = max(x2[v], x)

    def update_y(v, y):
        if v not in y1:
            y1[v] = y2[v] = y
        else:
            y1[v] = min(y1[v], y)
            y2[v] = max(y2[v], y)

    if d == 'R':
        update_x(+1, x)
        update_y(0, y)
    elif d == 'L':
        update_x(-1, x)
        update_y(0, y)
    elif d == 'U':
        update_x(0, x)
        update_y(+1, y)
    elif d == 'D':
        update_x(0, x)
        update_y(-1, y)


def area(t):
    xmin, xmax, ymin, ymax = INF, -INF, INF, -INF
    for (v, x) in list(x1.items()):
        xmin = min(xmin, x + v * t)
    for (v, x) in list(x2.items()):
        xmax = max(xmax, x + v * t)
    for (v, y) in list(y1.items()):
        ymin = min(ymin, y + v * t)
    for (v, y) in list(y2.items()):
        ymax = max(ymax, y + v * t)
    return (xmax - xmin) * (ymax - ymin)


ans = area(0)

x3 = list(x1.items()) + list(x2.items())
for i in range(len(x3)):
    for j in range(i + 1, len(x3)):
        if x3[i][0] != x3[j][0]:
            t = (x3[j][1] - x3[i][1]) // (x3[i][0] - x3[j][0])
            if t >= 0:
                ans = min(ans, area(t))

y3 = list(y1.items()) + list(y2.items())
for i in range(len(y3)):
    for j in range(i + 1, len(y3)):
        if y3[i][0] != y3[j][0]:
            t = (y3[j][1] - y3[i][1]) // (y3[i][0] - y3[j][0])
            if t >= 0:
                ans = min(ans, area(t))

print((ans / 4))
