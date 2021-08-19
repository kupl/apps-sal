def do(sh):
    return 1 - sh


a = [[1 for _ in range(5)] for __ in range(5)]
for i in range(1, 4):
    b = list(map(int, input().split()))
    for j in range(1, 4):
        if b[j - 1] % 2 == 1:
            a[i][j] = 1 - a[i][j]
            a[i + 1][j] = 1 - a[i + 1][j]
            a[i - 1][j] = 1 - a[i - 1][j]
            a[i][j + 1] = 1 - a[i][j + 1]
            a[i][j - 1] = 1 - a[i][j - 1]
print('\n'.join([''.join(map(str, line[1:-1])) for line in a[1:-1]]))
