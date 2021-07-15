import sys
sys.setrecursionlimit(1000000)

def dfs(color, u):
    for v in conn[u]:
        if not (color[v] == -1):
            continue
        color[v] = (color[u] + weight[(u, v)]) % 2
        dfs(color, v)

N = int(input())

conn = [[] for _ in range(N + 1)]
weight = {}
for _ in range(N - 1):
    u, v, w = list(map(int, input().split()))
    conn[u].append(v)
    conn[v].append(u)
    weight[(u, v)] = w
    weight[(v, u)] = w

color = [-1]*(N + 1)
color[1] = 0
dfs(color, 1)
for i in range(1, N + 1):
    print((color[i]))

