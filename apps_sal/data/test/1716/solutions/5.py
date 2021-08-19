import sys
(N, M, Q) = list(map(int, sys.stdin.readline().strip().split()))
cusum = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    (L, R) = list(map(int, sys.stdin.readline().strip().split()))
    cusum[L][R] += 1
for i in range(N):
    for j in range(N):
        cusum[i + 1][j + 1] += cusum[i + 1][j] + cusum[i][j + 1] - cusum[i][j]
for _ in range(Q):
    (p, q) = list(map(int, sys.stdin.readline().strip().split()))
    ans = cusum[q][q] - cusum[q][p - 1] - cusum[p - 1][q] + cusum[p - 1][p - 1]
    print(ans)
