n = int(input())
W = [[int(s) for s in input().split()] for _ in range(n)]
A = [[0 for _ in range(n)] for _ in range(n)]
B = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        A[i][j] = (W[i][j] + W[j][i]) / 2
        A[j][i] = A[i][j]
        B[i][j] = (W[i][j] - W[j][i]) / 2
        B[j][i] = -B[i][j]
print('\n'.join([' '.join([str(i) for i in x]) for x in A]))
print('\n'.join([' '.join([str(i) for i in x]) for x in B]))
