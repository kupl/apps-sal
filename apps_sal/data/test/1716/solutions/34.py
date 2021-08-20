import sys
readline = sys.stdin.readline
(N, M, Q) = list(map(int, readline().split()))
train = [[0] * (N + 1) for i in range(N + 1)]
for i in range(M):
    (L, R) = list(map(int, readline().split()))
    train[L][R] += 1
for i in range(N + 1):
    for j in range(1, N + 1):
        train[i][j] += train[i][j - 1]
for j in range(N + 1):
    for i in range(1, N + 1):
        train[i][j] += train[i - 1][j]
for i in range(Q):
    (p, q) = list(map(int, readline().split()))
    print(train[q][q] - train[p - 1][q] - train[q][p - 1] + train[p - 1][p - 1])
