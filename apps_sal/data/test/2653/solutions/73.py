import sys
sys.setrecursionlimit(10 ** 7)
(n, q) = map(int, input().split())
edge = [[] for _ in range(n)]
for i in range(n - 1):
    (x, y) = map(int, input().split())
    edge[x - 1].append(y - 1)
    edge[y - 1].append(x - 1)
ans = [0] * n
for i in range(q):
    (p, x) = map(int, input().split())
    ans[p - 1] += x


def dfs(c, p):
    for i in edge[c]:
        if i == p:
            continue
        ans[i] += ans[c]
        dfs(i, c)


dfs(0, -1)
print(*ans)
