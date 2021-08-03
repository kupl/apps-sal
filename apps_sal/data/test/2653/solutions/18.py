# abc138 D ki

import sys
sys.setrecursionlimit(10**6)

# def input():
#     return sys.stdin.readline()[:-1]

N, Q = map(int, input().split())
g = [[] for _ in range(N)]

point = [0] * N

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1
    point[a] += b


def dfs(n, pre=-1):
    for ne in g[n]:
        if ne == pre:
            continue

        point[ne] += point[n]

        dfs(ne, n)


dfs(0)
print(*point)
