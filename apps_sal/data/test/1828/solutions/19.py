n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append([x, y])
point_count = 0
for i in range(len(points) - 1):
    pre_point = points[i - 1]
    point = points[i]
    next_point = points[i + 1]
    if pre_point[0] == point[0] and next_point[1] == point[1]:
        if point[0] > next_point[0] and point[1] > pre_point[1] or point[0] < next_point[0] and point[1] < pre_point[1]:
            point_count += 1
    elif next_point[0] == point[0] and pre_point[1] == point[1]:
        if point[0] > pre_point[0] and point[1] < next_point[1] or point[0] < pre_point[0] and point[1] > next_point[1]:
            point_count += 1
print(point_count)
