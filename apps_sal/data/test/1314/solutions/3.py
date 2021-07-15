n = int(input())
minx = 1e9
miny = 1e9
for i in range(n):
    x, y = map(int, input().split())
    minx = min(minx, x)
    miny = min(miny, y)

maxx = -1e9
maxy = -1e9
for i in range(n):
    x, y = map(int, input().split())
    maxx = max(maxx, x)
    maxy = max(maxy, y)
print(minx + maxx, miny + maxy)
