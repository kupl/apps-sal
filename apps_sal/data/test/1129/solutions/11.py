n = int(input())
points = list(map(int, input().split()))
points.sort()
print(points[(len(points) - 1) // 2])
