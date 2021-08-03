def printMatrix(matrix):
    for matrixrow in matrix:
        row = ''
        for value in matrixrow:
            row += str(value) + ' '
        print(row)


n = int(input())
w = [[0 for i in range(n)] for i in range(n)]
a = [[0 for i in range(n)] for i in range(n)]
b = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    row = input().split(' ')
    for e in range(n):
        w[i][e] = int(row[e])
for i in range(n):
    for e in range(n):
        a[e][i] = a[i][e] = (w[i][e] + w[e][i]) / 2
        b[e][i] = w[e][i] - a[e][i]
printMatrix(a)
printMatrix(b)
