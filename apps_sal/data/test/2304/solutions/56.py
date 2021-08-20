import sys
sys.setrecursionlimit(200002)
(n, m) = list(map(int, input().split()))
graph = [[] for i in range(n)]
for i in range(m):
    (l, r, d) = list(map(int, input().split()))
    graph[l - 1].append([r - 1, d])
    graph[r - 1].append([l - 1, -d])


def dfs(s):
    for (t, d) in graph[s]:
        if x[t] is None:
            x[t] = x[s] + d
            if not dfs(t):
                return False
        elif x[t] - x[s] != d:
            return False
    return True


x = [None] * n
ans = True
for i in range(n):
    if x[i] is None:
        x[i] = 0
        if not dfs(i):
            ans = False
print(('No', 'Yes')[ans])
