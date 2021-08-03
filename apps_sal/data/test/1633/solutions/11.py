n, m, k = list(map(int, input().split()))
f = [[0 for i in range(m)] for j in range(n)]
move = [list(map(int, input().split())) for i in range(k)]
ans = 0
for i, mv in enumerate(move):
    f[mv[0] - 1][mv[1] - 1] = 1
    if mv[0] != 1 and mv[1] != 1:
        if f[mv[0] - 2][mv[1] - 2] + f[mv[0] - 2][mv[1] - 1] + f[mv[0] - 1][mv[1] - 2] == 3:
            ans = i + 1
            break
    if mv[0] != n and mv[1] != 1:
        if f[mv[0]][mv[1] - 2] + f[mv[0] - 1][mv[1] - 2] + f[mv[0]][mv[1] - 1] == 3:
            ans = i + 1
            break

    if mv[0] != 1 and mv[1] != m:
        if f[mv[0] - 2][mv[1]] + f[mv[0] - 2][mv[1] - 1] + f[mv[0] - 1][mv[1]] == 3:
            ans = i + 1
            break

    if mv[0] != n and mv[1] != m:
        if f[mv[0]][mv[1]] + f[mv[0]][mv[1] - 1] + f[mv[0] - 1][mv[1]] == 3:
            ans = i + 1
            break
print(ans)
