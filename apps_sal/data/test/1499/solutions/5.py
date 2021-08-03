n, m = [int(x) for x in input().split()]
M = [[0, 0, 0, 0] for i in range(n)]
for i in range(1, min(m, 2 * n) + 1, 2):
    M[i // 2][1] = i
for i in range(2, min(m, 2 * n) + 1, 2):
    M[i // 2 - 1][3] = i
for i in range(2 * n + 1, m + 1, 2):
    M[i // 2 - n][0] = i
for i in range(2 * n + 2, m + 1, 2):
    M[i // 2 - n - 1][2] = i
for i in range(n):
    for j in range(4):
        if M[i][j] != 0:
            print(M[i][j], end=' ')
