q = int(input())
for _ in range(q):
    d = [x for x in list(input())]
    (x, y) = (0, 0)
    (minX, maxX, minY, maxY) = (0, 0, 0, 0)
    (allowW, allowS, allowA, allowD) = (True, True, True, True)
    for v in d:
        if v == 'W':
            y += 1
            if y > maxY:
                maxY = y
                allowS = True
                allowW = False
            elif y == maxY:
                allowW = False
        elif v == 'S':
            y -= 1
            if y < minY:
                minY = y
                allowW = True
                allowS = False
            elif y == minY:
                allowS = False
        elif v == 'A':
            x -= 1
            if x < minX:
                minX = x
                allowA = False
                allowD = True
            elif x == minX:
                allowA = False
        else:
            x += 1
            if x > maxX:
                maxX = x
                allowA = True
                allowD = False
            elif x == maxX:
                allowD = False
    val = (maxX - minX + 1) * (maxY - minY + 1)
    if maxX - minX > 1 and (allowD or allowA):
        val = min(val, (maxX - minX) * (maxY - minY + 1))
    if maxY - minY > 1 and (allowW or allowS):
        val = min(val, (maxX - minX + 1) * (maxY - minY))
    print(val)
