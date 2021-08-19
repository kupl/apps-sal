n = int(input())
area = 0
(maxx, maxy, minx, miny) = (0, 0, 10 ** 5, 10 ** 5)
for i in range(0, n):
    (a, b, c, d) = list(map(int, input().split()))
    area += (c - a) * (d - b)
    maxx = max(maxx, c)
    minx = min(minx, a)
    maxy = max(maxy, d)
    miny = min(miny, b)
n = maxx - minx
if n == maxy - miny and n * n == area:
    print('YES')
else:
    print('NO')
