import sys
sys.setrecursionlimit(10 ** 6)


def input():
    return sys.stdin.readline()[:-1]


def dfs(v, prev=-1):
    for u in graph[v]:
        if u == prev:
            continue
        point[u] += point[v]
        dfs(u, v)


N, Q = list(map(int, input().split()))
graph = [[] for _ in range(N)]
point = [0] * N

for i in range(N - 1):
    a, b = list(map(int, input().split()))
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

for i in range(Q):
    p, x = list(map(int, input().split()))
    p -= 1
    point[p] += x

dfs(0)
print((*point))
