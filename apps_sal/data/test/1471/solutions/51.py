import sys
sys.setrecursionlimit(500 * 500)
n = int(input())
l = [list(map(int, input().split())) for _ in range(n - 1)]
g = [[] for _ in range(n)]
for i in l:
    v = i[0] - 1
    y = i[1] - 1
    w = i[2]
    g[v].append([y, w])
    g[y].append([v, w])
seen = [0] + [-1] * (n - 1)


def dfs(s):
    for k in g[s]:
        (v, w) = (k[0], k[1])
        if seen[v] != -1:
            continue
        seen[v] = seen[s] ^ w % 2
        dfs(v)


dfs(0)
for i in seen:
    print(i)
