n = int(input())


def area(width, height):
    return (width + 1) * (height + 1)


def calcul(s1, c, s2):
    maxx, maxy, minx, miny = 0, 0, 0, 0
    x, y = 0, 0
    for k in range(len(s1)):
        if s1[k] == "W":
            y += 1
        if s1[k] == "S":
            y -= 1
        if s1[k] == "A":
            x -= 1
        if s1[k] == "D":
            x += 1
        maxx = max(maxx, x)
        minx = min(minx, x)

        maxy = max(maxy, y)
        miny = min(miny, y)

    if c == "W":
        y += 1
    elif c == "S":
        y -= 1
    elif c == "A":
        x -= 1
    elif c == "D":
        x += 1
    else:
        print(c, "ok")

    maxx = max(maxx, x)
    minx = min(minx, x)

    maxy = max(maxy, y)
    miny = min(miny, y)

    for k in range(len(s2)):
        if s2[k] == "W":
            y += 1
        if s2[k] == "S":
            y -= 1
        if s2[k] == "A":
            x -= 1
        if s2[k] == "D":
            x += 1
        maxx = max(maxx, x)
        minx = min(minx, x)

        maxy = max(maxy, y)
        miny = min(miny, y)

    diffx = maxx - minx
    diffy = maxy - miny
    tmp = area(diffx, diffy)

    return tmp


def pre_calcul(s, moment, pre_avant, date_debut):
    x, y, maxx, minx, maxy, miny = pre_avant
    for k in range(date_debut, moment):
        if s[k] == "W":
            y += 1
        if s[k] == "S":
            y -= 1
        if s[k] == "A":
            x -= 1
        if s[k] == "D":
            x += 1
        maxx = max(maxx, x)
        minx = min(minx, x)

        maxy = max(maxy, y)
        miny = min(miny, y)

    return (x, y, maxx, minx, maxy, miny)


def calcul2(s, c, moment, precalcul):
    x, y, maxx, minx, maxy, miny = precalcul

    if c == "W":
        y += 1
    elif c == "S":
        y -= 1
    elif c == "A":
        x -= 1
    elif c == "D":
        x += 1
    else:
        print(c, "ok")

    maxx = max(maxx, x)
    minx = min(minx, x)

    maxy = max(maxy, y)
    miny = min(miny, y)

    for k in range(moment, len(s)):
        if s[k] == "W":
            y += 1
        if s[k] == "S":
            y -= 1
        if s[k] == "A":
            x -= 1
        if s[k] == "D":
            x += 1
        maxx = max(maxx, x)
        minx = min(minx, x)

        maxy = max(maxy, y)
        miny = min(miny, y)

    diffx = maxx - minx
    diffy = maxy - miny
    tmp = area(diffx, diffy)

    return tmp


for _ in range(n):
    s = input()
    maxx, maxy, minx, miny = 0, 0, 0, 0
    x, y = 0, 0
    momentminx, momentmaxx, momentminy, momentmaxy = -1, -1, -1, -1
    for k in range(len(s)):
        if s[k] == "W":
            y += 1
        if s[k] == "S":
            y -= 1
        if s[k] == "A":
            x -= 1
        if s[k] == "D":
            x += 1

        if x > maxx:
            momentmaxx = k
        if y > maxy:
            momentmaxy = k
        if x < minx:
            momentminx = k
        if y < miny:
            momentminy = k
        maxx = max(maxx, x)
        minx = min(minx, x)

        maxy = max(maxy, y)
        miny = min(miny, y)
    diffx = maxx - minx
    diffy = maxy - miny

    tmp = 999999999999999999999999999999999999
    l = [momentmaxx, momentmaxy, momentminx, momentminy]
    l = list(set(l))
    l = [i for i in l if i != -1]
    l.sort()
    if l != []:
        precalcul = pre_calcul(s, l[0], (0, 0, 0, 0, 0, 0), 0)
        avant = l[0]
        for moment in l:
            precalcul = pre_calcul(s, moment, precalcul, avant)
            avant = moment
            tmp = min(tmp, calcul2(s, 'W', moment, precalcul))
            tmp = min(tmp, calcul2(s, 'S', moment, precalcul))
            tmp = min(tmp, calcul2(s, 'A', moment, precalcul))
            tmp = min(tmp, calcul2(s, 'D', moment, precalcul))
    print(tmp)
