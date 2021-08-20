from math import hypot, atan2
N = int(input())
XY = [tuple(map(int, input().split())) for i in range(N)]
xy = sorted(XY, key=lambda x: atan2(x[1], x[0]))
xy += xy
ans = 0
for i in range(N):
    sx = sy = 0
    for j in range(N):
        (x, y) = xy[i + j]
        sx += x
        sy += y
        d = hypot(sx, sy)
        if d > ans:
            ans = d
print(ans)
