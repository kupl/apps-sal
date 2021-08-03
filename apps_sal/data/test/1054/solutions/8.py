
n = int(input())


max_r = 0

x, y = map(int, input().split())
minX = x
maxX = x
minY = y
maxY = y
for i in range(n - 1):
    x, y = map(int, input().split())
    minX = min(minX, x)
    maxX = max(maxX, x)
    minY = min(minY, y)
    maxY = max(maxY, y)

print(max(maxX - minX, maxY - minY) ** 2)
