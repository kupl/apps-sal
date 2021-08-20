(N, M) = map(int, input().split())
path_matrix = []
for i in range(N):
    path_matrix.append([False] * N)
for i in range(M):
    (a, b) = map(int, input().split())
    path_matrix[a - 1][b - 1] = True
    path_matrix[b - 1][a - 1] = True
view = [False] * N


def path(x, depth):
    if view[x - 1]:
        return False
    if depth == N - 1:
        return True
    view[x - 1] = True
    total_ans = 0
    for i in range(N):
        if path_matrix[x - 1][i]:
            total_ans += int(path(i + 1, depth + 1))
    view[x - 1] = False
    return total_ans


print(path(1, 0))
