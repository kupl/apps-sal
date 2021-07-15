n, k = [int(x) for x in input().split()]
M1 = [[i + n*j for j in range(k-1)] for i in range(1, n+1)]
M2 = [[(k-1)*n + i*(n-k+1) + j for j in range(1, n-k+2)] for i in range(0, n)]
M = [M1[i] + M2[i] for i in range(n)]
print((n-k+1)*(n-1)*n // 2 + ((k-1)*n + 1)*n)
for i in range(n):
    for j in range(n):
        print(M[i][j], end = ' ')
    print()

