

def getmaxpath(g, v, par):
    maxp = 0
    for u, c in g[v]:
        if u == par:
            continue
        maxp = max(maxp, c + getmaxpath(g, u, v))
    return maxp


n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, c = (int(x) for x in input().split())
    g[u].append((v, c,))
    g[v].append((u, c,))
print(getmaxpath(g, 0, -1))
