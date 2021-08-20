import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
INF = 2 ** 30
n = int(input())
P = list(map(int, input().split()))
T = [[] for _ in range(n)]
for (i, p) in enumerate(P, 1):
    T[p - 1].append(i)
X = tuple(map(int, input().split()))
D = [-1] * n


def dfs(v):
    if D[v] != -1:
        return D[v]
    l = len(T[v])
    x = X[v]
    dp = [INF] * (x + 1)
    dp[0] = 0
    for nv in T[v]:
        k = [INF] * (x + 1)
        d = dfs(nv)
        for j in range(x + 1):
            if j >= X[nv]:
                k[j] = min(k[j], dp[j - X[nv]] + d)
            if j >= d:
                k[j] = min(k[j], dp[j - d] + X[nv])
        dp = tuple(k)
    res = min(dp)
    D[v] = res
    return res


ans = dfs(0)
if ans == INF:
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')
