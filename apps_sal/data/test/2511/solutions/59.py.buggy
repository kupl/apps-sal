# Review problem

from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
N, K = map(int, input().split())
graph = [[] for i in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0 for i in range(N + 1)]
dis = [0 for i in range(N + 1)]
parent = [-1 for i in range(N + 1)]
parent[1] = -1
visited[1] = True
mod = 10**9 + 7


def bfs(node):
    for child in graph[node]:
        if visited[child] == False:
            visited[child] = True
            parent[child] = node
            dis[child] = dis[node] + 1
            bfs(child)


bfs(1)

par_data = defaultdict(int)
for i in range(1, N + 1):
    x = parent[i]
    par_data[x] += 1
ans = K
for parent in par_data.keys():
    if parent > 0:
        X = par_data[parent]
        if parent == 1:
            for i in range(X):
                ans = ans * (K - 1 - i)
                ans %= mod
                if ans == 0:
                    print(0)
                    return
        else:
            for i in range(X):
                ans = ans * (K - 2 - i)
                ans %= mod
                if ans == 0:
                    print(0)
                    return
print(ans)
