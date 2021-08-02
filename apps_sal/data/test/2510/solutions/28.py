import sys
sys.setrecursionlimit(1000000)


f = lambda: map(int, input().split())
N, M = f()

if M == 0:
    print(1)
    return

G = [set() for _ in range(N + 1)]
for _ in range(M):
    a, b = f()
    G[a].add(b)
    G[b].add(a)
# print(G)

d = {}
F = [0] * (N + 1)


def dfs(i, n):
    if F[i]: return
    F[i] = 1
    for g in G[i]:
        if F[g]: continue
        t = d.get(n, set())
        t.add(g)
        d[n] = t
        dfs(g, n)


for i in range(1, N + 1):
    dfs(i, i)

print(max(len(i) for i in d.values()) + 1)
