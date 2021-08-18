input_str = input()
n, m = int(input_str.split()[0]), int(input_str.split()[1])
a = []
points_wall = []
points = 0
temp = list(map(int, input().split()))
a.append(temp)
pos = temp.index(1) if temp.count(1) else -1
if pos != -1:
    points_wall.append([pos, 0])
for i in range(n - 2):
    temp = list(map(int, input().split()))
    if temp[0]:
        points_wall.append([0, i + 1])
    if temp[m - 1]:
        points_wall.append([m - 1, i + 1])
    points += temp[1:m - 1].count(1)
    a.append(temp)
temp = list(map(int, input().split()))
a.append(temp)
pos = temp.index(1) if temp.count(1) else -1
if pos != -1:
    points_wall.append([pos, n - 1])


def count(matr, x):
    c = 0
    for i in range(len(matr)):
        c += matr[i].count(x)
    return c


if len(points_wall):
    print(2)
else:
    if points:
        print(4)
