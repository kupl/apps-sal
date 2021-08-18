N, M = map(int, input().split())

path_matrix = []

for n in range(N):
    path_matrix.append([False] * N)

for m in range(M):
    line = map(int, input().split())
    paths = [x - 1 for x in line]
    path_matrix[paths[0]][paths[1]] = True
    path_matrix[paths[1]][paths[0]] = True

visited = [False] * N


def dfs(now, depth):
    if visited[now]:
        return 0
    if depth == N - 1:
        return 1

    visited[now] = True
    total_paths = 0
    for i in range(0, N):
        if path_matrix[now][i]:
            total_paths += dfs(i, depth + 1)

    visited[now] = False

    return total_paths


print(dfs(0, 0))
