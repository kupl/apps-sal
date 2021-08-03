dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]
n = int(input())
arr = [['c' for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if j != 0 and arr[i][j - 1] == 'W':
            arr[i][j] = 'B'
        elif i == 0 and j == 0:
            arr[i][j] = 'W'
        elif j == 0 and arr[i - 1][j] == 'W':
            arr[i][j] = 'B'
        else:
            arr[i][j] = 'W'
for i in range(n):
    for j in range(n):
        print(arr[i][j], end='')
    print()
