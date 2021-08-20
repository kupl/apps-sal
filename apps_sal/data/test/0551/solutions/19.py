points = int(input())
y = list(map(int, input().split()))


def slope(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def passes(one, two, point):
    return 0 == one[0] * (two[1] - point[1]) + two[0] * (point[1] - one[1]) + point[0] * (one[1] - two[1])


def possible(start, joint, coords):
    others = list()
    for point in coords:
        if not passes(start, joint, point):
            others.append(point)
    if len(others) == 0:
        return (False, others)
    elif len(others) == 1:
        return (True, others)
    elif len(others) >= 2:
        (other1, other2) = (others[0], others[1])
        for point in others:
            if not passes(other1, other2, point):
                return (False, others)
        if slope(other1, other2) == slope(start, joint):
            return (True, others)
        else:
            return (False, others)


coords = [(k + 1, y[k]) for k in range(points)]
start = coords.pop(0)
(poss, others) = possible(start, coords[0], coords)
if not poss and len(others) > 0:
    poss |= possible(start, others[0], coords)[0]
if not poss:
    poss |= possible(coords[0], coords[1], coords + [start])[0]
if poss:
    print('Yes')
else:
    print('No')
