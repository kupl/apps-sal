points = []
mx = 0
for i in range(3):
    points.append(list(map(int, input().split())))

points = sorted(points, key=lambda x: x[0])
k = 1
x, y = points[0][0], points[0][1]
x2, y2 = points[1][0], points[1][1]
coor = [[points[0][0], points[0][1]]]
mx = y
mn = y
while True:
    if x < x2:
        x += 1
    elif y < y2:
        y += 1
        mx = y
    elif y > y2:
        y -= 1
        mn = y
    else:
        break
    k += 1
    coor.append([x, y])
x3, y3 = points[2][0], points[2][1]
if mn <= y3 <= mx:
    y = y3
elif y3 < mn:
    y = mn
elif y3 > mx:
    y = mx
while True:
    if y < y3:
        y += 1
    elif y > y3:
        y -= 1
    elif x < x3:
        x += 1
    else:
        break
    k += 1
    coor.append([x, y])
print(k)
for i in coor:
    print(*i)
