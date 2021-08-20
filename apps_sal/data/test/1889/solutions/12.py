(n, m, q) = [int(x) for x in input().split()]
data = []
saveCount = []
globalMax = 0
globalMaxIndex = -1
for i in range(n):
    temp = [int(x) for x in input().split()]
    mx = 0
    curEyes = 0
    for j in range(m):
        if temp[j] == 1:
            curEyes += 1
            if curEyes > mx:
                mx = curEyes
        else:
            curEyes = 0
    saveCount.append(mx)
    if mx > globalMax:
        globalMaxIndex = i
        globalMax = mx
    data.append(temp)
for i in range(q):
    (y, x) = [int(c) - 1 for c in input().split()]
    data[y][x] = 0 if data[y][x] else 1
    mx = 0
    curEyes = 0
    if y == globalMaxIndex:
        saveCount[y] = 0
        globalMax = 0
        for j in range(n):
            if saveCount[j] > globalMax:
                globalMax = saveCount[j]
                globalMaxIndex = j
    for j in range(m):
        if data[y][j] == 1:
            curEyes += 1
            if curEyes > mx:
                mx = curEyes
        else:
            curEyes = 0
    if mx > globalMax:
        print(mx)
        globalMax = mx
        globalMaxIndex = y
    else:
        print(globalMax)
    saveCount[y] = mx
