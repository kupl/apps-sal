N, M, Q = map(int, input().split())
trains = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    L, R = map(int, input().split())
    trains[L][R] += 1
for i in range(1, N + 1):
    for j in range(1, N + 1):
        trains[i][j] += trains[i - 1][j]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        trains[i][j] += trains[i][j - 1]
ans = [0] * Q
for k in range(Q):
    p, q = map(int, input().split())
    ans[k] = trains[q][q] - trains[p-1][q] - trains[q][p-1] + trains[p-1][p-1]
for A in ans:
    print(A)
