import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())


def dfs(s, p):
    nonlocal ans
    for t, w in g[s]:
        if t == p or ans[t] >= 0:
            continue
        ans[t] = ans[s] ^ (w % 2)
        dfs(t, s)


g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append((v, w))
    g[v].append((u, w))

ans = [-1] * n
ans[0] = 0
dfs(0, -1)
print(*ans, sep="\n")
