import sys
sys.setrecursionlimit(10 ** 7)
N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    (u, v, w) = list(map(int, input().split()))
    u -= 1
    v -= 1
    graph[u].append([v, w])
    graph[v].append([u, w])
color = [-1] * N


def even(v=0, col=0):
    color[v] = col
    for i in range(len(graph[v])):
        (nv, nw) = list(map(int, graph[v][i]))
        if color[nv] != -1:
            continue
        if nw % 2 == 0:
            even(nv, col)
        else:
            even(nv, 1 - col)


even()
for i in range(N):
    print(color[i])
