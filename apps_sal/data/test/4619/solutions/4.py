
w, h, n = map(int, input().split())
points = []
area = [0, w, 0, h]

for i in range(n):
    x, y, a = map(int, input().split())
    points.append([x, y, a])

for i in range(n):
    if points[i][2] == 1:
        area[0] = max(area[0], points[i][0])
    if points[i][2] == 2:
        area[1] = min(area[1], points[i][0])
    if points[i][2] == 3:
        area[2] = max(area[2], points[i][1])
    if points[i][2] == 4:
        area[3] = min(area[3], points[i][1])

ans = max(0, (area[1] - area[0])) * max(0, (area[3] - area[2]))

print(ans)
