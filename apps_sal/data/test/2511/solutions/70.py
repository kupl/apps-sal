mod = 10 ** 9 + 7
import sys
sys.setrecursionlimit(10 ** 7)
def dfs(u):
    cnt = 0
    res = 1
    for i in edges[u]:
        if visited[i] == -1:
            visited[i] = 0
            cnt += 1
            res *= dfs(i)
            res %= mod
    for i in range(cnt):
        res *= k - i - 2
        res %= mod
    return res
n, k = map(int, input().split())
edges = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)
visited = [-1] * n
visited[0] = 0
ans = k
for i in range(len(edges[0])):
    ans *= (k - i - 1)
    ans %= mod
for i in edges[0]:
    visited[i] = 0
    ans *= dfs(i)
    ans %= mod
print(ans)
