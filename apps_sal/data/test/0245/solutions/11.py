n = int(input())
area = 0
minx = miny = 999999
maxx = maxy = 0
for _ in range(n):
    x1, y1, x2, y2 = list(map(int, input().split()))
    minx = min(minx, min(x1, x2))
    miny = min(miny, min(y1, y2))
    maxx = max(maxx, max(x1, x2))
    maxy = max(maxy, max(y1, y2))
    a = abs(x1 - x2) * abs(y1 - y2)
    area += a

h = maxy - miny
w = maxx - minx

if h != w or h*h != area:
    print('NO')
else:
    print('YES')
