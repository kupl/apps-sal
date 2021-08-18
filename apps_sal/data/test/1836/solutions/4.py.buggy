import sys


def dfs(v):
    nonlocal g, links, used, tail, val
    used[v] = True

    maxv = 1
    for u in g[v]:
        if not used[u]:
            # maxv = max(maxv, dfs(u) + 1)    -  было used вместо not used в условии
            dfs(u)
        maxv = max(maxv, tail[u] + 1)
    val[v] = links[v] * maxv
    tail[v] = maxv
    # return maxv


# fin = open("cfr338b.in", "r")
fin = sys.stdin

n, m = map(int, fin.readline().split())

g = [[] for i in range(n)]
links = [0] * n

for i in range(m):
    u, v = map(int, fin.readline().split())
    u, v = (u - 1, v - 1) if u <= v else (v - 1, u - 1)
    # g[u].append(v)
    g[v].append(u)
    links[v] += 1
    links[u] += 1

used = [False] * n
val, tail = [0] * n, [0] * n
maxv = 0

for i in range(n):
    if not used[i]:
        dfs(i)
    maxv = max(maxv, val[i])

print(maxv)
