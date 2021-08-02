import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
G = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b, c = map(int, input().split())
    G[a].append([b, c])
    G[b].append([a, c])

q, k = map(int, input().split())


D = [None] * (n + 1)


def dfs(x, d):
    D[x] = d
    for yy, dd in G[x]:
        if D[yy] is not None:
            continue
        dfs(yy, dd + d)


dfs(k, 0)

for i in range(q):
    x, y = map(int, input().split())
    print(D[x] + D[y])
