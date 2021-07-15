N = int(input())
string = ['D' for i in range(N)]
matrix = [['*' for i in range(N)]]
matrix[0][N // 2] = 'D'
matrix += [['*'] * N for i in range(N - 1)]
for i in range(1, N):
    for j in range(1, N - 1):
        if matrix[i - 1][j] == 'D' or matrix[i - 1][j - 1] == 'D' or matrix[i - 1][j + 1] == 'D':
            matrix[i][j] = 'D'
for i in matrix[:N // 2]:
    print(''.join(i))
print(''.join(string))
for i in range(N // 2 - 1, -1, -1):
    print(''.join(matrix[i]))

