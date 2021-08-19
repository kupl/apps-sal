n = int(input())
minX = 1000000005
minY = minX
maxX = -1000000005
maxY = maxX
for i in range(n):
    (t, t2) = list(map(int, input().split()))
    minY = min(minY, t2)
    maxY = max(maxY, t2)
    minX = min(minX, t)
    maxX = max(maxX, t)
print(max(maxX - minX, maxY - minY) ** 2)
