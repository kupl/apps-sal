def dfs(place, target):
    vis[place] = True
    if target == place:
        total[0] += 1
        return()
    anyAdj = 0
    for i in j[place]:
        if not vis[i]:
            anyAdj = 1
            dfs(i, target)
    if anyAdj == 0:
        return()


v, e = list(map(int, input().split()))
edges = []
for i in range(e):
    edges.append(list(map(int, input().split())))
colors = []
for i in edges:
    colors.append(i[2])
colors = list(set(colors))
colorAdjs = []
for i in colors:
    colorAdjs.append([[] for w in range(v)])
    for j in edges:
        if j[2] == i:
            colorAdjs[-1][j[0] - 1].append(j[1] - 1)
            colorAdjs[-1][j[1] - 1].append(j[0] - 1)
q = int(input())
for i in range(q):
    total = [0]
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    for j in colorAdjs:
        vis = [False] * v
        dfs(a, b)
    print(total[0])
