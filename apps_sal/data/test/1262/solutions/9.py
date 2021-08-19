import sys
reader = (list(map(int, s.split())) for s in sys.stdin)
(n,) = next(reader)
xy = []
for _ in range(n):
    (x, y) = next(reader)
    xy.append([x, y])
c = list(next(reader))
k = list(next(reader))
graph = [[0 for _ in range(n + 1)] for _i in range(n + 1)]
for i in range(n):
    for j in range(i + 1, n):
        cost = (abs(xy[i][0] - xy[j][0]) + abs(xy[i][1] - xy[j][1])) * (k[i] + k[j])
        graph[i][j] = graph[j][i] = cost
    graph[n][i] = graph[i][n] = c[i]


def primMST():
    key = [1000000000000] * (n + 1)
    parent = [None] * (n + 1)
    key[0] = 0
    mstSet = [False] * (n + 1)
    parent[0] = -1
    for cout in range(n + 1):
        mn = 1000000000000
        for v in range(n + 1):
            if key[v] < mn and mstSet[v] == False:
                mn = key[v]
                min_index = v
        u = min_index
        mstSet[u] = True
        for v in range(n + 1):
            if graph[u][v] > 0 and mstSet[v] == False and (key[v] > graph[u][v]):
                key[v] = graph[u][v]
                parent[v] = u
    vss = 0
    cost = 0
    for i in range(1, n + 1):
        if parent[i] == n or i == n:
            vss += 1
        cost += graph[i][parent[i]]
    myprint = sys.stdout.write
    myprint(str(cost) + '\n')
    myprint(str(vss) + '\n')
    vs = [0] * vss
    es = [[]] * (n - vss)
    (k1, k2) = (0, 0)
    for i in range(1, n + 1):
        if parent[i] == n:
            vs[k1] = i + 1
            k1 += 1
        elif i == n:
            vs[k1] = parent[i] + 1
            k1 += 1
        else:
            es[k2] = [i + 1, parent[i] + 1]
            k2 += 1
    [myprint(str(st) + ' ') for st in vs]
    myprint('\n')
    myprint(str(len(es)) + '\n')
    [myprint(str(i[0]) + ' ' + str(i[1]) + '\n') for i in es]


primMST()
