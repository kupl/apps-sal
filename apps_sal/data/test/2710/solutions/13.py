from collections import deque
from sys import stdin, stdout

maxNum = 200000


def retrieveFlow(theMap):
    countNodes = len(theMap)
    parent = [-1] * countNodes
    ans = 0
    while bfs(theMap, parent):
        curr_flow = maxNum + 1
        temp = countNodes - 1
        while temp != 0:
            curr_flow = min(curr_flow, theMap[parent[temp]][temp])
            temp = parent[temp]
        ans += curr_flow
        temp = countNodes - 1
        while temp != 0:
            par = parent[temp]
            theMap[par][temp] -= curr_flow
            theMap[temp][par] += curr_flow
            temp = par
    return ans


def bfs(theMap, parent):
    queue = deque([])
    queue.append(0)
    countNodes = len(theMap)
    beenThere = [False] * countNodes
    beenThere[0] = True

    while queue:
        temp = queue.popleft()
        for i in range(countNodes):
            if theMap[temp][i] > 0 and (not beenThere[i]):
                queue.append(i)
                beenThere[i] = True
                parent[i] = temp
                if i == countNodes - 1:
                    return True
    return beenThere[countNodes - 1]


def soldierTraveling():
    n, m = [int(_) for _ in stdin.readline().rstrip().split()]
    readAll = stdin.readlines()
    firstNum = [int(_) for _ in readAll[0].split()]
    LastNum = [int(_) for _ in readAll[1].split()]

    if sum(LastNum) != sum(firstNum):
        stdout.write('NO\n')
        return

    theMap = [[0] * (n * 2 + 2) for _ in range(n * 2 + 2)]
    theEdges = [(_, _) for _ in range(1, n + 1)]

    for i in range(n):
        theMap[0][i + 1] = firstNum[i]
        theMap[n + i + 1][n * 2 + 2 - 1] = LastNum[i]
        theMap[i + 1][n + i + 1] = firstNum[i]

    for index in range(m):
        i, j = [int(_) for _ in readAll[2 + index].split()]
        theMap[i][n + j] = firstNum[i - 1]
        theMap[j][n + i] = firstNum[j - 1]
        theEdges.append((i, j))

    theMaxFlow = retrieveFlow(theMap)

    if sum(firstNum) != theMaxFlow:
        stdout.write('NO\n')
        return

    tempM = [[0] * n for _ in range(n)]

    for (i, j) in theEdges:
        tempM[i - 1][j - 1] = firstNum[i - 1] - theMap[i][n + j]
        tempM[j - 1][i - 1] = firstNum[j - 1] - theMap[j][n + i]
    stdout.write('YES\n')

    for i in tempM:
        stdout.write(' '.join(str(_) for _ in i))
        stdout.write('\n')


soldierTraveling()
stdout.close()
