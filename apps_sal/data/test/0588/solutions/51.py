import math
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
l.sort(key=lambda x: math.atan2(x[1], x[0]))
l += l
ans = 0
for i in range(n):
    x = y = 0
    for j in range(n):
        (nx, ny) = l[i + j]
        x += nx
        y += ny
        ans = max(ans, (x ** 2 + y ** 2) ** 0.5)
print(ans)
