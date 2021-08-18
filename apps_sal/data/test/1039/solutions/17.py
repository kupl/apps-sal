from collections import deque


N = int(input())

ARR = [list(map(int, input().split())) for i in range(N - 1)]

Q, K = map(int, input().split())

BRR = [list(map(int, input().split())) for i in range(Q)]


def prepare(n, arr):
    links = {}
    nodeStatus = {}
    distances = {}
    finalDistance = {}
    for i in range(1, N + 1):
        nodeStatus.__setitem__(i, False)
        finalDistance.__setitem__(i, 0)

    for i in range(len(arr)):
        tmp = arr[i]
        startNode = tmp[0]
        endNode = tmp[1]
        distance = tmp[2]
        distances.__setitem__((startNode, endNode), distance)
        distances.__setitem__((endNode, startNode), distance)
        if links.get(startNode) == None:
            links.__setitem__(startNode, [endNode])
        else:
            tmpChild = links.get(startNode)
            tmpChild.append(endNode)
            links.__setitem__(startNode, tmpChild)

        if links.get(endNode) == None:
            links.__setitem__(endNode, [startNode])
        else:
            tmpChild = links.get(endNode)
            tmpChild.append(startNode)
            links.setdefault(endNode, tmpChild)
    return links, nodeStatus, distances, finalDistance


def bfs(startNode):
    q = deque()

    q.append((startNode, 0))

    while len(q):
        currentNode, dist = q.popleft()
        finalDistance.__setitem__(currentNode, dist)
        nodeStatus.__setitem__(currentNode, True)

        childNodes = links.get(currentNode)

        for childNode in childNodes:
            if nodeStatus.get(childNode) == False:
                q.append((childNode, dist + distances.get((currentNode, childNode))))


links, nodeStatus, distances, finalDistance = prepare(N, ARR)


bfs(K)
for i in range(Q):
    dist1 = finalDistance[BRR[i][0]]
    dist2 = finalDistance[BRR[i][1]]
    print(dist1 + dist2)
