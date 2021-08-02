n = int(input())
W = [[int(i) for i in input().split()] for _ in range(n)]
A = [[0 for __ in range(n)] for _ in range(n)]
B = [[0 for __ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        A[i][j] = (W[i][j] + W[j][i]) / 2
        A[j][i] = A[i][j]
        B[i][j] = W[i][j] - A[i][j]
        B[j][i] = -B[i][j]
for i in A:
    print(*i)
for i in B:
    print(*i)
