from math import sqrt
(N, R) = map(int, input().split())
disk_xs = map(int, input().split())
disks = []
for x in disk_xs:
    y = R
    for (x0, y0) in disks:
        sq = 4 * R ** 2 - (x0 - x) ** 2
        if sq >= 0:
            y1 = y0 + sqrt(sq)
            y = max(y, y1)
    disks.append((x, y))
print(' '.join(map(lambda x: str(x[1]), disks)))
