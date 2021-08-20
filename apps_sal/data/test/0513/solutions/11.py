def check():
    l = []
    for i in range(8):
        (x, y) = list(map(int, input().split()))
        l += [[x, y]]
    xSet = set()
    ySet = set()
    for (x, y) in l:
        xSet.add(x)
        ySet.add(y)
    if len(xSet) != 3 or len(ySet) != 3:
        return False
    xList = sorted(list(xSet))
    yList = sorted(list(ySet))
    z = []
    for x in xList:
        for y in yList:
            if x == xList[1] and y == yList[1]:
                pass
            else:
                z += [[x, y]]
    z.sort()
    l.sort()
    return z == l


if check():
    print('respectable')
else:
    print('ugly')
