import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, k = list(map(int, input().split()))
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = list([int(x) - 1 for x in input().split()])
    edges[a].append(b)
    edges[b].append(a)
MOD = 10**9 + 7
INF = 10**10
dp = [INF] * n


def dfs(v, parent, x):
    dp[v] = x
    if parent == -1:
        next_x = k - 1
    else:
        next_x = k - 2
    for v2 in edges[v]:
        if v2 == parent:
            continue
        dfs(v2, v, next_x)
        next_x -= 1


dfs(0, -1, k)
ans = 1
for x in dp:
    ans = ans * x % MOD
print(ans)
