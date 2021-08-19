N, M = map(int, input().split())

path = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    path[a][b] = 1
    path[b][a] = 1

visited = [0] * (N + 1)


def dfs(now, depth):
    if visited[now]:
        return 0
    if depth == N:
        return 1  # 最後まで探索したらはじめて+1

    visited[now] = 1

    total_paths = 0

    for i in range(1, N + 1):
        if path[now][i]:
            total_paths += dfs(i, depth + 1)

    visited[now] = 0

    return total_paths


print(dfs(1, 1))
