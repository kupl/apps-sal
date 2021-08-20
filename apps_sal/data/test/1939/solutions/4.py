(n, k) = list(map(int, input().split()))
A = [['0' for i in range(n)] for j in range(n)]
for i in range(n):
    A[i][i] = str(k)
for row in A:
    print(' '.join(row))
