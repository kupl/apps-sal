import heapq
n, m, k = list(map(int, input().split()))
connectionList = []
for _ in range(n):
    connectionList.append([])
edgeList = []
for _ in range(m):
    x, y, w = list(map(int, input().split()))
    edgeList.append((x, y, w))
edgeList.sort(key=lambda x: x[2])
if k < m:
    maxDist = edgeList[min(m, k) - 1][2]
else:
    maxDist = sum([x[2] for x in edgeList])
colorList = {}
colorVertex = []
for i in range(n):
    colorList[i] = [i]
    colorVertex.append(i)

for i in range(min(m, k)):
    x, y, w = edgeList[i]
    connectionList[x - 1].append((y - 1, w))
    connectionList[y - 1].append((x - 1, w))
    if colorVertex[x - 1] != colorVertex[y - 1]:
        if len(colorList[colorVertex[x - 1]]) >= len(colorList[colorVertex[y - 1]]):
            prevColor = colorVertex[y - 1]
            for elem in colorList[colorVertex[y - 1]]:
                colorVertex[elem] = colorVertex[x - 1]
                colorList[colorVertex[x - 1]].append(elem)
            del colorList[prevColor]
        else:
            prevColor = colorVertex[x - 1]
            for elem in colorList[colorVertex[x - 1]]:
                colorVertex[elem] = colorVertex[y - 1]
                colorList[colorVertex[y - 1]].append(elem)
            del colorList[prevColor]

pathList = []
for key in colorList:
    vertexList = colorList[key]
    for mainVertex in vertexList:
        vertexPQueue = []
        isCovered = {}
        distanceDic = {}
        for elem in vertexList:
            isCovered[elem] = False
            distanceDic[elem] = maxDist
        isCovered[mainVertex] = True
        for elem in connectionList[mainVertex]:
            heapq.heappush(vertexPQueue, (elem[1], elem[0]))
            distanceDic[elem[0]] = elem[1]
        while vertexPQueue:
            distance, curVertex = heapq.heappop(vertexPQueue)
            if isCovered[curVertex]:
                continue
            elif distance >= maxDist:
                break
            for elem in connectionList[curVertex]:
                if distance + elem[1] < distanceDic[elem[0]]:
                    heapq.heappush(vertexPQueue, (distance + elem[1], elem[0]))
                    distanceDic[elem[0]] = distance + elem[1]
        for key in distanceDic:
            if distanceDic[key] <= maxDist and key > mainVertex:
                pathList.append(distanceDic[key])
        if len(pathList) > k:
            pathList.sort()
            pathList = pathList[0:k]
            if pathList[-1] < maxDist:
                maxDist = pathList[-1]
pathList.sort()
print(pathList[k - 1])
