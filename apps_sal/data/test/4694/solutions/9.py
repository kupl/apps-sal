N = int(input())
points = list(map(int, input().split()))

result = max(points) - min(points)
print(result)
