n = int(input())
maxx = maxy = -10 ** 10
minx = miny = 10 ** 10
for i in range(n):
    (x, y) = list(map(int, input().split()))
    if x > maxx:
        maxx = x
    if y > maxy:
        maxy = y
    if y < miny:
        miny = y
    if x < minx:
        minx = x
print(max(maxx - minx, maxy - miny) ** 2)
