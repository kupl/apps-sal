(n, m, q) = list(map(int, input().split()))
ruiseki = [[0 for i in range(n + 1)] for i in range(n + 1)]
for i in range(m):
    (l, r) = list(map(int, input().split()))
    ruiseki[l][r] = ruiseki[l][r] + 1
for i in range(0, n + 1):
    for j in range(1, n + 1):
        ruiseki[i][j] = ruiseki[i][j] + ruiseki[i][j - 1]
for i in range(1, n + 1):
    for j in range(n + 1):
        ruiseki[i][j] = ruiseki[i - 1][j] + ruiseki[i][j]
for i in range(q):
    (p, q) = list(map(int, input().split()))
    print(ruiseki[q][q] - ruiseki[p - 1][q] - ruiseki[q][p - 1] + ruiseki[p - 1][p - 1])
