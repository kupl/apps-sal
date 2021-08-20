n = int(input())
(minx, maxx, miny, maxy) = (10 ** 10, -10 ** 10, 10 ** 10, -10 ** 10)
for i in range(n):
    (x, y) = list(map(int, input().split()))
    if x > maxx:
        maxx = x
    if y > maxy:
        maxy = y
    if x < minx:
        minx = x
    if y < miny:
        miny = y
print(max(maxx - minx, maxy - miny) ** 2)
