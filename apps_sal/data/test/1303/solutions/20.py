(p, q, l, r) = list(map(int, input().split()))
bestMoments = 0


def enter(stringNum):
    res = []
    for st in range(stringNum):
        (a, b) = list(map(int, input().split()))
        for i in range(a, b + 1):
            res.append(i)
    return res


littleY = []
littleZ = []
littleY = enter(p)
littleZ = enter(q)
lenYandZ = len(littleY) + len(littleZ)
for i in range(l, r + 1):
    currentZ = list([x + i for x in littleZ])
    if len(set(currentZ + littleY)) < lenYandZ:
        bestMoments += 1
print(bestMoments)
