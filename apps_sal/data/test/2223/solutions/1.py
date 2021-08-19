import collections


def getIntList():
    return list(map(int, input().split()))


def getTransIntList(n):
    first = getIntList()
    m = len(first)
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        result[i][0] = first[i]
    for j in range(1, n):
        curr = getIntList()
        for i in range(m):
            result[i][j] = curr[i]
    return result


n = int(input())
if n > 1:
    u, v = getTransIntList(n - 1)
    for i in range(n - 1):
        u[i] -= 1
        v[i] -= 1


def solve1(n, u, v):
    nears = [set() for _ in range(n)]
    for i in range(n - 1):
        v1, v2 = u[i], v[i]
        nears[v1].add(v2)
        nears[v2].add(v1)
    prev = [0] * n
    nexts = [set() for _ in range(n)]
    level = [0] * n
    vStart = 0
    VertToCheck = collections.deque([vStart])
    AllVerts = collections.deque()

    def defineNextPrev(vert):
        for v1 in nears[vert]:
            if v1 != prev[vert]:
                nexts[vert].add(v1)
                prev[v1] = vert
                level[v1] = level[vert] + 1
                VertToCheck.append(v1)
    while len(VertToCheck) > 0:
        currVert = VertToCheck.popleft()
        AllVerts.append(currVert)
        defineNextPrev(currVert)
    cutFlag = [False] * n
    result = -1
    while len(AllVerts) > 0:
        vert = AllVerts.pop()
        for v1 in nexts[vert]:
            #print(cutFlag[vert], cutFlag[v1]);
            cutFlag[vert] = cutFlag[v1] == cutFlag[vert]
            # print(cutFlag[vert])
        if cutFlag[vert]:
            result += 1
    return result


if n % 2 == 1:
    print(-1)
else:
    print(solve1(n, u, v))
