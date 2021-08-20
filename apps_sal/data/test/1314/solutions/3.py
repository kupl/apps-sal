n = int(input())
minx = 1000000000.0
miny = 1000000000.0
for i in range(n):
    (x, y) = map(int, input().split())
    minx = min(minx, x)
    miny = min(miny, y)
maxx = -1000000000.0
maxy = -1000000000.0
for i in range(n):
    (x, y) = map(int, input().split())
    maxx = max(maxx, x)
    maxy = max(maxy, y)
print(minx + maxx, miny + maxy)
