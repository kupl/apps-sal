(N, M, Q) = list(map(int, input().split()))
cnt = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    (L, R) = list(map(int, input().split()))
    cnt[L][R] += 1
for i in range(N):
    for j in range(N):
        cnt[i + 1][j + 1] += cnt[i + 1][j] + cnt[i][j + 1] - cnt[i][j]
for _ in range(Q):
    (p, q) = list(map(int, input().split()))
    print(cnt[q][q] - cnt[q][p - 1] - cnt[p - 1][q] + cnt[p - 1][p - 1])
