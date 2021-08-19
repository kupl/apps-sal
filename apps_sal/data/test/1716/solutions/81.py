(N, M, Q) = list(map(int, input().split()))
T = [tuple(map(int, input().split())) for i in range(M)]
queries = [tuple(map(int, input().split())) for i in range(Q)]
plot = [[0] * (N + 1) for i in range(N + 1)]
accum = [[0] * (N + 1) for i in range(N + 1)]
for (Li, Ri) in T:
    plot[Li][Ri] += 1
for i in range(1, N + 1):
    for j in range(1, N + 1):
        accum[i][j] = accum[i][j - 1] + accum[i - 1][j] - accum[i - 1][j - 1] + plot[i][j]
for (pi, qi) in queries:
    print(accum[qi][qi] - accum[pi - 1][qi])
