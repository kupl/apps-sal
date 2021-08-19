import sys
n = int(sys.stdin.readline())
A = [[0] * n for i in range(n)]
for i in range(n):
    I = sys.stdin.readline().split()
    for j in range(n):
        A[i][j] = int(I[j])
B = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        B[i][j] = (A[i][j] + A[j][i]) / 2
        print(B[i][j], end=' ')
    print()
for i in range(n):
    for j in range(n):
        print(A[i][j] - B[i][j], end=' ')
    print()
