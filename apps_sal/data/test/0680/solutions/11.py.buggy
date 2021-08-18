def func(m, n, key):
    nonlocal x, y
    x0 = m
    y0 = n
    if key == 1:
        for j in range(abs(x - m)):
            if x > m:
                print(x0, y0)
                x0 += 1
            else:
                print(x0, y0)
                x0 -= 1
        for j in range(abs(y - n)):
            if abs(y - y0) > ymin:
                if y > n:
                    print(x0, y0)
                    y0 += 1
                else:
                    print(x0, y0)
                    y0 -= 1
    else:
        for j in range(abs(y - n)):
            if y > n:
                print(x0, y0)
                y0 += 1
            else:
                print(x0, y0)
                y0 -= 1
        for j in range(abs(x - m)):
            if abs(x - x0) > xmin:
                if x > m:
                    print(x0, y0)
                    x0 += 1
                else:
                    print(x0, y0)
                    x0 -= 1


x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
x3, y3 = list(map(int, input().split()))
x = sorted([x1, x2, x3])[1]
y = sorted([y1, y2, y3])[1]
xmin = min(abs(x - x1), abs(x - x2), abs(x - x3))
ymin = min(abs(y - y1), abs(y - y2), abs(y - y3))
print(abs(x - x1) + abs(x - x2) + abs(x - x3) + abs(y - y1) + abs(y - y2) + abs(y - y3) + 1 - max(xmin, ymin))
if xmin < ymin:
    key = 1
    for i in range(ymin):
        print(x, y + i + 1)
        print(x, y - i - 1)
else:
    key = -1
    for i in range(xmin):
        print(x + xmin + 1, y)
        print(x - xmin - 1, y)
func(x1, y1, key)
func(x2, y2, key)
func(x3, y3, key)
print(x, y)
