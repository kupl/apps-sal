n = int(input())
A = [[0 for i in range(n)] for j in range(n)]
B = [[0 for i in range(n)] for j in range(n)]
W = []
for i in range(n):
    s = list(map(int, input().split()))
    W.append(s)
for i in range(n):
    for j in range(i, n):
        if i == j:
            A[i][j] = W[i][j]
        else:
            sred = (W[i][j] + W[j][i]) / 2
            A[i][j] = sred
            A[j][i] = sred
            B[i][j] = W[i][j] - sred
            B[j][i] = W[j][i] - sred
for i in A:
    print(*i)
for i in B:
    print(*i)
