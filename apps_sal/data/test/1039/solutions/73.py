import sys
sys.setrecursionlimit(20000000)
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

N = int(input())

ARR = [list(map(int, input().split())) for i in range(N - 1)]

Q, K = map(int, input().split())

BRR = [list(map(int, input().split())) for i in range(Q)]


def prepare(arr, n):
    links = [[] for i in range(n)]
    depth = [0 for i in range(n)]
    for i in range(n - 1):
        startNode = arr[i][0] - 1
        endNode = arr[i][1] - 1
        dist = arr[i][2]

        links[startNode].append((endNode, dist))
        links[endNode].append((startNode, dist))

    return links, depth


def dfs(currentNode, parrentNode=-1, dist=0):
    childNodes = links[currentNode]
    depths[currentNode] = dist
    for (childNode, childDistance) in childNodes:
        if childNode == parrentNode:
            continue

        dfs(childNode, currentNode, dist + childDistance)


links, depths = prepare(ARR, N)

dfs(K - 1)

for i in range(Q):
    p1 = BRR[i][0] - 1
    p2 = BRR[i][1] - 1

    d1 = depths[p1]
    d2 = depths[p2]

    print(d1 + d2)
