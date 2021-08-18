lst = list(map(int, input().strip().split()))
n = lst[0]
m = lst[1]
corners = [[1, 1], [1, m], [n, m], [n, 1]]
point = [lst[2], lst[3]]
a = lst[4]
b = lst[5]
corners2 = []
for corner in corners:
    if (corner[0] - point[0]) % a == 0 and (corner[1] - point[1]) % b == 0 and corner not in corners2:
        corners2.append(corner)
corners.clear()


if not corners2:
    print("Poor Inna and pony!")
else:
    for i in range(len(corners2)):
        corner = corners2[i]
        if point in corners2:
            corners.append(0)
        else:
            move1 = abs(corner[0] - point[0]) // a
            move2 = abs(corner[1] - point[1]) // b
            if (move1 - move2) % 2 == 0 and (point[0] + a in range(1, n + 1) or point[0] - a in range(1, n + 1)) and (point[1] + b in range(1, m + 1) or point[1] - b in range(1, m + 1)):
                corners.append(max(move1, move2))
    if not corners:
        print("Poor Inna and pony!")
    else:
        print(min(corners))
