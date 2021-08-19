import copy
(N, M) = map(int, input().split())
path_matrix = [[0 for i in range(N)] for j in range(N)]
L = [[] for i in range(M)]
for i in range(M):
    (a, b) = map(int, input().split())
    path_matrix[a - 1][b - 1] = 1
    path_matrix[b - 1][a - 1] = 1
    L[i].append(a)
    L[i].append(b)
color_white = ['W' for i in range(N)]
color_black = ['B' for i in range(N)]
visited = copy.deepcopy(color_white)


def path(x, y):
    path_matrix[x - 1][y - 1] = 0
    path_matrix[y - 1][x - 1] = 0
    return DFS(x, path_matrix)


def DFS(x, tim):
    visited[x - 1] = 'B'
    if visited == color_black:
        return True
    total_ans = 0
    for i in range(N):
        if tim[x - 1][i] == 1 and visited[i] == 'W':
            total_ans = int(DFS(i + 1, tim))
    return total_ans


ans = 0
for i in range(M):
    visited = copy.deepcopy(color_white)
    if path(L[i][0], L[i][1]) == 0:
        ans += 1
    path_matrix[L[i][0] - 1][L[i][1] - 1] = 1
    path_matrix[L[i][1] - 1][L[i][0] - 1] = 1
print(ans)
