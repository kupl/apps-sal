inp = input().split()
x = int(inp[0])
y = int(inp[1])


def distance(points):
    d = 0
    for i in range(len(points) - 1):
        p1 = points[i]
        p2 = points[i + 1]
        d += ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
    return d


res = None
poss = []
if x != 0 and y != 0:
    poss.append([(0, 1), (x, y), (0, 0), (x, y - 1)])
    poss.append([(1, 0), (x, y), (0, 0), (x - 1, y)])
    poss.append([(0, 0), (x, y), (x, 0), (0, y)])
    poss.append([(0, 0), (x, y), (0, y), (x, 0)])
    d1 = distance(poss[0])
    d2 = distance(poss[1])
    d3 = distance(poss[2])
    d4 = distance(poss[3])
    if d1 >= d2 and d1 >= d3 and (d1 >= d4):
        res = poss[0]
    elif d2 >= d1 and d2 >= d3 and (d2 >= d4):
        res = poss[1]
    elif d3 >= d1 and d3 >= d2 and (d3 >= d4):
        res = poss[2]
    else:
        res = poss[3]
elif x == 0 and y != 0:
    res = [(0, 1), (0, y), (0, 0), (0, y - 1)]
elif x != 0 and y == 0:
    res = [(1, 0), (x, 0), (0, 0), (x - 1, 0)]
else:
    res = [(0, 0), (0, 0), (0, 0), (0, 0)]
for i in res:
    print(i[0], i[1])
