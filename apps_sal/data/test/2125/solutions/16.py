(n, m) = list(map(int, input().split()))
board = [input() for _ in range(n)]
u = [[1 for _ in range(m)] for _ in range(n)]
l = [[1 for _ in range(m)] for _ in range(n)]
for i in range(1, n):
    for j in range(m):
        if board[i][j] == board[i - 1][j]:
            u[i][j] = u[i - 1][j] + 1
for j in range(1, m):
    for i in range(n):
        if board[i][j] == board[i][j - 1]:
            l[i][j] = l[i][j - 1] + 1
output = 0
for i1 in range(n):
    for j in range(m):
        k = u[i1][j]
        i2 = i1 - k
        if i2 >= 0 and u[i2][j] == k:
            i3 = i2 - k
            if i3 >= 0 and u[i3][j] >= k:
                output += min((l[i][j] for i in range(i3 - k + 1, i1 + 1)))
print(output)
