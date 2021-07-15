x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))

dx = abs(x1 - x2)
dy = abs(y1 - y2)

print(max(dx, dy))

