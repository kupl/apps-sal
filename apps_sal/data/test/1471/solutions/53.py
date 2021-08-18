import sys
sys.setrecursionlimit(10**7)
n = int(input())
es = [[] for i in range(n)]
for i in range(n - 1):
    u, v, w = list(map(int, input().split()))
    es[u - 1].append([v, w])
    es[v - 1].append([u, w])

colors = [0 for i in range(n)]


def dfs(v, color):
    colors[v - 1] = color
    for i in es[v - 1]:
        if i[1] % 2 == 0 and colors[i[0] - 1] == 0:
            dfs(i[0], color)
        elif i[1] % 2 == 1 and colors[i[0] - 1] == 0:
            dfs(i[0], (-1) * color)
    return colors


a = dfs(1, -1)
for i in a:
    if i == -1:
        print((0))
    else:
        print((1))
