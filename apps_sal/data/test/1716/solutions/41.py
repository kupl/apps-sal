(N, M, Q) = list(map(int, input().split()))
X = [[0] * N for _ in range(N)]
for i in range(M):
    (L, R) = list(map(int, input().split()))
    L -= 1
    R -= 1
    X[L][R] += 1
S = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(N):
        S[i + 1][j + 1] = S[i][j + 1] + S[i + 1][j] - S[i][j] + X[i][j]
for i in range(Q):
    (p, q) = list(map(int, input().split()))
    p -= 1
    ans = S[q][q] - S[p][q] - S[q][p] + S[p][p]
    print(ans)
