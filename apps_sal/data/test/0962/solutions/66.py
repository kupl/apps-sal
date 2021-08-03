import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
seen = [False] * n


def dfs(v):
    seen[v] = True
    for nv in G[v]:
        nxt[v] = nv
        if seen[nv]:
            return nv
        s = dfs(nv)
        if s != -1:
            return s
    seen[v] = False
    return -1


for i in range(n):
    nxt = [-1] * n
    s = dfs(i)
    if s != -1:
        break
else:
    print(-1)
    return
while True:
    used = set()
    L = []
    while s not in used:
        used.add(s)
        L.append(s)
        s = nxt[s]
    L.append(s)
    for i in range(len(L) - 1):
        a, b = L[i], L[i + 1]
        for nv in G[a]:
            if nv != b and nv in used:
                nxt[a] = nv
                s = a
                break
        else:
            continue
        break
    else:
        print(len(used))
        for v in used:
            print(v + 1)
        break
