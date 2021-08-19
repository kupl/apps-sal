xmin, ymin, xmax, ymax, a = 31400, 31400, 0, 0, 0

for i in range(int(input())):

    x1, y1, x2, y2 = map(int, input().split())

    xmin = min(xmin, x1)

    ymin = min(ymin, y1)

    xmax = max(xmax, x2)

    ymax = max(ymax, y2)

    a += (x2 - x1) * (y2 - y1)

# print(xmax,xmin,ymax,ymin,a,end="")
print('YES' if xmax - xmin == ymax - ymin and a == (xmax - xmin) ** 2 else 'NO')
