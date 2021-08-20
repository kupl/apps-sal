import sys
sys.setrecursionlimit(pow(10, 6))
readline = sys.stdin.readline


def dfs(nw, d):
    V[nw] = d
    for nx in G[nw]:
        if V[nx[0]] == -1:
            dfs(nx[0], d + nx[1])


n = int(readline())
G = [[] for _ in range(n)]
for i in range(n - 1):
    (a, b, c) = map(int, readline().split())
    G[a - 1].append((b - 1, c))
    G[b - 1].append((a - 1, c))
(q, k) = map(int, readline().split())
V = [-1] * n
dfs(k - 1, 0)
for i in range(q):
    (x, y) = map(lambda x: int(x) - 1, readline().split())
    print(V[x] + V[y])
