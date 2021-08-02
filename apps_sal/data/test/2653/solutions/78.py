import sys
sys.setrecursionlimit(10**9)
n, q = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

subtree_size = [0] * n
cnt = [0] * n

for _ in range(q):
    p, x = map(int, input().split())
    p -= 1
    cnt[p] += x
ans = [0] * n


def dfs(G, v, p):
    ans[v] += cnt[v]
    for nv in G[v]:
        if nv == p:
            continue
        cnt[nv] += cnt[v]
        dfs(G, nv, v)

    subtree_size[v] = 1
    for c in G[v]:
        if c == p:
            continue
        subtree_size[v] += subtree_size[c]


root = 0
dfs(G, root, -1)

for i in range(n):
    print(ans[i], end=' ')
