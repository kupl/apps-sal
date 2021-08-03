def put(x1, y1, x2, y2):
    mass2 = []
    if y1 == y2:
        for i in range(x1 + 1, x2):
            mass2.append((i, y1))
    elif y2 > y1:
        for i in range(x1 + 1, x2 + 1):
            mass2.append((i, y1))
        for i in range(y1 + 1, y2):
            mass2.append((x2, i))
    else:
        for i in range(x1 + 1, x2 + 1):
            mass2.append((i, y1))
        for i in range(y2 + 1, y1):
            mass2.append((x2, i))
    return mass2


def best(x1, y1, x2, y2, x3, y3):
    mass = []
    mass += put(x1, y1, x2, y2)
    if y2 > y1:
        if y3 > y2:
            mass += put(x2, y2, x3, y3)
        elif y3 <= y2 and y3 >= y1:
            mass += put(x2, y3, x3, y3)
        else:
            mass += put(x2, y1, x3, y3)
    elif y2 == y1:
        mass += put(x2, y2, x3, y3)
    else:
        if y3 > y1:
            mass += put(x2, y1, x3, y3)
        elif y3 <= y1 and y3 >= y2:
            mass += put(x2, y3, x3, y3)
        else:
            mass += put(x2, y2, x3, y3)
    for i in [(x1, y1), (x2, y2), (x3, y3)]:
        if i not in mass:
            mass.append(i)
    print(len(mass))
    for i in mass:
        print(*i)


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
a = [(x1, y1), (x2, y2), (x3, y3)]
a.sort()
c = best(a[0][0], a[0][1], a[1][0], a[1][1], a[2][0], a[2][1])
