def is_parallel(p1, p2):
    if p1[0] == p2[0]:
        return 1
    if p1[1] == p2[1]:
        return 2
    return 0


a = [list(map(int, input().split())) for _ in range(3)]

all_the_same = is_parallel(a[0], a[1]) == is_parallel(a[1], a[2]) == is_parallel(a[0], a[2])
first_and_second = is_parallel(a[0], a[1])
if all_the_same:
    if first_and_second != 0:
        print(1)
        return
    else:
        print(3)
else:
    new_points = []

    for i in range(3):
        if is_parallel(a[i], a[(i + 1) % 3]):
            for j in range(3):
                new_points.append(a[(i + j) % 3])
            break

    if len(new_points) == 0:
        print(3)
        return

    if is_parallel(*new_points[:2]) == 2:
        for i in range(3):
            new_points[i][0], new_points[i][1] = new_points[i][1], new_points[i][0]

    if new_points[0][1] > new_points[1][1]:
        new_points[0], new_points[1] = new_points[1], new_points[0]

    if new_points[2][1] <= new_points[0][1] <= new_points[1][1]:
        print(2)
    elif new_points[0][1] <= new_points[1][1] <= new_points[2][1]:
        print(2)
    else:
        print(3)
