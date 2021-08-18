def check(index):
    point1 = points[index]
    count = 0
    for point in points:
        if point[1] == point1[1]:
            count += 1
    if count == 1:
        return False
    count = 0
    for point in points:
        if point[0] == point1[0]:
            count += 1
    if count == 1:
        return False


n = int(input())
points = []
for i in range(4 * n + 1):
    x, y = map(int, input().split())
    points.append((x, y))
index = 0
max_x = count1 = max_y = count2 = count3 = count4 = 0
min_x = min_y = 51
for point in points:
    if point[0] > max_x:
        max_x = point[0]
    if point[0] < min_x:
        min_x = point[0]
    if point[1] > max_y:
        max_y = point[1]
    if point[1] < min_y:
        min_y = point[1]
for point in points:
    if point[0] == max_x:
        count1 += 1
    if point[0] == min_x:
        count2 += 1
    if point[1] == max_y:
        count3 += 1
    if point[1] == min_y:
        count4 += 1
if count1 == 1:
    for point in points:
        if point[0] == max_x:
            print(point[0], point[1])
            return
if count2 == 1:
    for point in points:
        if point[0] == min_x:
            print(point[0], point[1])
            return
if count3 == 1:
    for point in points:
        if point[1] == max_y:
            print(point[0], point[1])
            return
if count4 == 1:
    for point in points:
        if point[1] == min_y:
            print(point[0], point[1])
            return
for point in points:
    if point[0] != max_x and point[0] != min_x and point[1] != max_y and point[1] != min_y:
        print(point[0], point[1])
        return
