(N, M, Q) = map(int, input().split())
mem = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    (L, R) = map(int, input().split())
    mem[L - 1][R - 1] += 1
for L in range(N):
    for R in range(1, N):
        mem[L][R] += mem[L][R - 1]
for R in range(N):
    for L in range(1, N):
        mem[L][R] += mem[L - 1][R]
res = []
for _ in range(Q):
    (QL, QR) = map(int, input().split())
    if QL == 1:
        r = mem[QR - 1][QR - 1]
    else:
        r = mem[QR - 1][QR - 1] - mem[QL - 2][QR - 1]
    res.append(r)
for r in res:
    print(r)
