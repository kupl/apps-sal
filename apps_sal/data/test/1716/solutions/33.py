n, m, q = list(map(int, input().split()))
lr = [[0 for i in range(n + 1)] for j in range(n + 1)]
for i in range(m):
    l, r = list(map(int, input().split()))
    lr[l][r] = lr[l][r] + 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        lr[i][j] = lr[i][j - 1] + lr[i][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        lr[i][j] = lr[i][j] + lr[i - 1][j]
for i in range(q):
    p, q = list(map(int, input().split()))
    print((lr[q][q] - lr[p - 1][q] - lr[q][p - 1] + lr[p - 1][p - 1]))
