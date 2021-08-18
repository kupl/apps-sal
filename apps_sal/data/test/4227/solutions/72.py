import sys
n, m = list(map(int, input().split()))
es = [[0 for i in range(n)] for i in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    es[a - 1][b - 1] = 1
    es[b - 1][a - 1] = 1

sys.setrecursionlimit(10**7)


visited = [0 for i in range(n)]
check = [1 for i in range(n)]


def dfs(v, visited):
    ans = 0
    visited[v - 1] = 1

    if visited == check:
        visited[v - 1] = 0
        return 1
    for i in range(n):
        if es[v - 1][i] == 1 and visited[i] == 0:
            ans += dfs(i + 1, visited)
    visited[v - 1] = 0
    return ans


print((dfs(1, visited)))
