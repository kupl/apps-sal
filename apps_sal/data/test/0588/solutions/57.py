import math
n = int(input())
XY = [list(map(int, input().split())) for i in range(n)]
XY.sort(key=lambda x: math.atan2(x[1], x[0]))
XY += XY
ans = 0
for i in range(n):
    x = 0
    y = 0
    for j in range(n):
        (nx, ny) = XY[i + j]
        x += nx
        y += ny
        ans = max(ans, (x ** 2 + y ** 2) ** 0.5)
print(ans)
