import math
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
point = []
r = 0
for i in range(n - 1):
    (x1, y1) = xy[i]
    for j in range(i + 1, n):
        (x2, y2) = xy[j]
        d = ((x1 - x2) / 2) ** 2 + ((y1 - y2) / 2) ** 2
        if r ** 2 > d:
            if y1 - y2 != 0:
                a = -(x1 - x2) / (y1 - y2)
                x = math.sqrt((r ** 2 - d) / (a ** 2 + 1)) // 10 ** (-6) * 10 ** (-6)
                point.append([(x1 + x2) / 2 + x, (y1 + y2) / 2 + a * x])
                point.append([(x1 + x2) / 2 - x, (y1 + y2) / 2 - a * x])
            else:
                x = math.sqrt(r ** 2 - d) // 1 // 10 ** (-6) * 10 ** (-6)
                point.append([(x1 + x2) / 2, (y1 + y2) / 2 + x])
                point.append([(x1 + x2) / 2, (y1 + y2) / 2 - x])
        elif r ** 2 == d:
            point.append([(x1 + x2) / 2, (y1 + y2) / 2])
r_o = 800
r_i = 0
while r_o - r_i > 10 ** (-8):
    judge = 0
    while point:
        (x, y) = point.pop()
        c = 0
        for (i, j) in xy:
            if (x - i) ** 2 + (y - j) ** 2 > r ** 2:
                c = 1
                break
        if c == 0:
            judge = 1
            break
    if judge == 1:
        r_o = r
    else:
        r_i = r
    r = (r_o + r_i) / 2
    point = []
    for i in range(n - 1):
        (x1, y1) = xy[i]
        for j in range(i + 1, n):
            (x2, y2) = xy[j]
            d = ((x1 - x2) / 2) ** 2 + ((y1 - y2) / 2) ** 2
            if r ** 2 > d:
                if y1 - y2 != 0:
                    a = -(x1 - x2) / (y1 - y2)
                    x = math.sqrt((r ** 2 - d) / (a ** 2 + 1)) // 10 ** (-6) * 10 ** (-6)
                    point.append([(x1 + x2) / 2 + x, (y1 + y2) / 2 + a * x])
                    point.append([(x1 + x2) / 2 - x, (y1 + y2) / 2 - a * x])
                else:
                    x = math.sqrt(r ** 2 - d) // 10 ** (-6) * 10 ** (-6)
                    point.append([(x1 + x2) / 2, (y1 + y2) / 2 + x])
                    point.append([(x1 + x2) / 2, (y1 + y2) / 2 - x])
            elif r ** 2 == d:
                point.append([(x1 + x2) / 2, (y1 + y2) / 2])
print(r)
