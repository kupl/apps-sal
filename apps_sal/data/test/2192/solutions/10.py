n = int(input())
W = list()
for i in range(n):
    W.append([int(x) for x in input().split()])
A = [[0 for x in range(n)] for x in range(n)]
B = [[0 for x in range(n)] for x in range(n)]
for i in range(n):
    B[i][i] = W[i][i]
for i in range(n):
    for j in range(i, n):
        A[i][j] = (W[i][j] + W[j][i]) / 2
        B[i][j] = W[i][j] - A[i][j]
    for j in range(i):
        B[i][j] = -B[j][i]
        A[i][j] = A[j][i]
for i in range(n):
    print(' '.join((str(x) for x in A[i])))
for i in range(n):
    print(' '.join((str(x) for x in B[i])))
