from collections import deque
#
# N = 5
# ARR = [
#     [1, 2, 1],
#     [1, 3, 1],
#     [2, 4, 1],
#     [3, 5, 1]
# ]
#
# Q, K = 3, 1
#
# BRR = [
#     [2, 4],
#     [2, 3],
#     [4, 5],
# ]
#
#
# N = 7
# ARR = [
#     [1, 2, 1],
#     [1, 3, 3],
#     [1, 4, 5],
#     [1, 5, 7],
#     [1, 6, 9],
#     [1, 7, 11],
# ]
#
# Q, K = 3, 2
#
# BRR = [
#     [1, 3],
#     [4, 5],
#     [6, 7],
# ]
#
#
# N = 10
# ARR = [
#     [1, 2, 1000000000],
#     [2, 3, 1000000000],
#     [3, 4, 1000000000],
#     [4, 5, 1000000000],
#     [5, 6, 1000000000],
#     [6, 7, 1000000000],
#     [7, 8, 1000000000],
#     [8, 9, 1000000000],
#     [9, 10, 1000000000]
# ]
#
# Q, K = 1, 1
#
# BRR = [
#     [9, 10]
# ]


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

# print(links)
# print(nodeStatus)
# print(distances)
# print(finalDistance)


bfs(K)
for i in range(Q):
    dist1 = finalDistance[BRR[i][0]]
    dist2 = finalDistance[BRR[i][1]]
    print(dist1 + dist2)
