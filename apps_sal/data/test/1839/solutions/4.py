n = int(input())
li = [[0] * n for i in range(n)]
for i in range(n * n):
    a, b = [int(i) for i in input().split()]
    if (li[a - 1][b - 1] == 0):
        for j in range(n):
            li[j][b - 1] = 1
            li[a - 1][j] = 1
        print(i + 1, end=' ')
