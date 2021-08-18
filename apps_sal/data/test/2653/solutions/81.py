import sys
sys.setrecursionlimit(10 ** 6)


def input():
    return sys.stdin.readline()[:-1]


N, Q = map(int, input().split())
graph = [[] for _ in range(N)]
point = [0] * N
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
for _ in range(Q):
    a, b = map(int, input().split())
    a = a - 1
    point[a] += b


def dfs(now, prev=-1):
    for next in graph[now]:
        if next == prev:
            continue
        point[next] += point[now]
        dfs(next, now)


dfs(0)
print(*point)
