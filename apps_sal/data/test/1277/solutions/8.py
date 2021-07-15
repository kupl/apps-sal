import sys
sys.setrecursionlimit(10**6)
n, a, b = list(map(int, input().split()))
D = [[0]*2 for _ in range(101010)]
E = [[] for _ in range(n)]


def dfs(cur, pre, d, id):
    D[cur][id] = d
    for nv in E[cur]:
        if nv != pre:
            dfs(nv, cur, d+1, id)


a -= 1
b -= 1
for i in range(n-1):
    x, y = list(map(int, input().split()))
    x -= 1
    y -= 1
    E[x].append(y)
    E[y].append(x)
dfs(a, a, 0, 0)
dfs(b, b, 0, 1)
max_d = 0
for i in range(n):
    if D[i][0] < D[i][1]:
        max_d = max(max_d, D[i][1]-1)
print(max_d)

