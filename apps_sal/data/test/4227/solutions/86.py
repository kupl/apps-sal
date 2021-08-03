import sys
sys.setrecursionlimit(10 ** 6)

N, M = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for i in range(M):
    a, b = [int(x) - 1 for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)


def dfs(cur, visited):
    if visited == (1 << N) - 1:
        return 1
    res = 0
    for to in graph[cur]:
        if not (visited >> to) & 1:
            res += dfs(to, visited | (1 << to))
    return res


print((dfs(0, 1)))
