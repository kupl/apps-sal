import sys
sys.setrecursionlimit(10 ** 9)
N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    (a, b, c) = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))
(Q, K) = map(int, input().split())
visited = [0 for _ in range(N)]


def DFS(a, b, c):
    for (i, j) in graph[b]:
        if i != a:
            visited[i] = c + j
            DFS(b, i, c + j)


DFS(-1, K - 1, 0)
for _ in range(Q):
    (x, y) = map(int, input().split())
    print(visited[x - 1] + visited[y - 1])
