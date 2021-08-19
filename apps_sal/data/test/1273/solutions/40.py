from collections import deque


def readinput():
    n = int(input())
    nList = []
    for _ in range(n + 1):
        nList.append([])
    edges = []
    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        edges.append((a, b))
        nList[a].append(b)
        nList[b].append(a)
    return n, nList, edges


def bfs(s, nList):
    # print(nList)
    WHITE = 0
    GRAY = 1
    BLACK = 2
    status = [WHITE] * (n + 1)
    parent = [0] * (n + 1)
    color = [0] * (n + 1)
    maxcolor = 0
    Q = deque([])
    Q.append(s)
    while(len(Q) > 0):
        u = Q.popleft()
        usedcolor = color[u]
        col = 1
        for t in nList[u]:
            if status[t] == WHITE:
                status[t] = GRAY
                parent[t] = u
                if col == usedcolor:
                    col += 1
                color[t] = col
                Q.append(t)
                col += 1
        maxcolor = max(maxcolor, col - 1)
        status[u] = BLACK
        # print(u,usedcolor)
    return color, maxcolor


def main(n, nList, edges):
    color, maxcolor = bfs(1, nList)
    print(maxcolor)
    for a, b in edges:
        print((color[b]))


def __starting_point():
    n, nList, edges = readinput()
    main(n, nList, edges)


__starting_point()
