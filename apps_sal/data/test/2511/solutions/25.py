import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


def dfs(v, p, k):
    ret = 1
    if len(graph[v]) > k:
        return 0
    kc = k - 2
    if p == -1:
        kc = k - 1
    for vi in graph[v]:
        if vi != p:
            ret *= kc
            ret = ret % mod
            kc -= 1
    for vi in graph[v]:
        if vi != p:
            ret *= dfs(vi, v, k)
            ret = ret % mod
    return ret


(n, k) = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    (a, b) = list(map(int, input().split()))
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
print(dfs(0, -1, k) * k % mod)
