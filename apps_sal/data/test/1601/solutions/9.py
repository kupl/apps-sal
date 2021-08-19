n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))
    points[i].append(i + 1)
points.sort()
rem = []
i = 0
while i < len(points):
    if i < len(points) - 1 and points[i][:2] == points[i + 1][:2]:
        print(points[i][3], points[i + 1][3])
        i += 2
    else:
        rem.append(points[i])
        i += 1
points = list(rem)
rem = []
i = 0
while i < len(points):
    if i < len(points) - 1 and points[i][0] == points[i + 1][0]:
        print(points[i][3], points[i + 1][3])
        i += 2
    else:
        rem.append(points[i])
        i += 1
points = list(rem)
rem = []
i = 0
while i < len(points) - 1:
    print(points[i][3], points[i + 1][3])
    i += 2
