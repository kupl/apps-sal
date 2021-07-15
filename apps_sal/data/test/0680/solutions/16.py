def doWay(x, y, x1, y1, x2, y2):
    nonlocal answer
    while x < x1 and x < x2:
        x += 1
        answer.add((x, y))
    while y < y1 and y < y2:
        y += 1
        answer.add((x, y))
    while x > x1 and x > x2:
        x -= 1
        answer.add((x, y))
    while y > y1 and y > y2:
        y -= 1
        answer.add((x, y))


xy = list()
xy.append(tuple(map(int, input().split())))
xy.append(tuple(map(int, input().split())))
xy.append(tuple(map(int, input().split())))

answer = set(xy)
doWay(xy[0][0], xy[0][1], xy[1][0], xy[1][1], xy[2][0], xy[2][1])
doWay(xy[1][0], xy[1][1], xy[0][0], xy[0][1], xy[2][0], xy[2][1])
doWay(xy[2][0], xy[2][1], xy[0][0], xy[0][1], xy[1][0], xy[1][1])

print(len(answer))
for x, y in answer:
    print(x, y)
