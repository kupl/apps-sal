import sys
sys.setrecursionlimit(10 ** 9)


def dfs(i):
    if reached[i] == 1:
        return
    reached[i] = 1
    for dic in uv[i]:
        to = dic['to']
        w = dic['weight']
        if w % 2 == 0:
            color[to] = color[i]
        else:
            color[to] = int(not color[i])
        dfs(to)


n = int(input())
color = [0] * (n + 1)
reached = [0] * (n + 1)
uv = [[] * (n + 1) for i in range(n + 1)]
for i in range(n - 1):
    (u, v, w) = map(int, input().split())
    uv[u].append({'to': v, 'weight': w})
    uv[v].append({'to': u, 'weight': w})
dfs(1)
for i in color[1:]:
    print(i)
