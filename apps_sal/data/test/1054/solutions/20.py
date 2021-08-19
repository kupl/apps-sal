n = int(input())
(pointx, pointy) = ([], [])
for i in range(n):
    (x, y) = map(int, input().split())
    pointx.append(x)
    pointy.append(y)
ans = max(max(pointx) - min(pointx), max(pointy) - min(pointy))
print(ans * ans)
