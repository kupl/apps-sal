N = int(input())
XY = [[int(_) for _ in input().split()] for _ in range(N)]
ans = -1
for dx, dy in ((1, 1), (-1, 1), (-1, -1), (1, -1)):
    xy2 = [x * dx + y * dy for x, y in XY]
    ans = max(ans, max(xy2) - min(xy2))
print(ans)
