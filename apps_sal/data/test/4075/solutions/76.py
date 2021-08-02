N, M = map(int, input().split())
A = [[0 for _ in range(N)] for _ in range(M)]
for i in range(M):
    S = list(map(int, input().split()))
    for j in S[1:]:
        A[i][j - 1] = 1

P = list(map(int, input().split()))

ans = 0
for bit in range(2**N):
    b = bin(bit)[2:].zfill(N)
    X = [0] * M
    for i in range(M):
        for j in range(N):
            if A[i][j] == 1 and b[j] == '1':
                X[i] = (X[i] + 1) % 2

    tmp = 0
    for i in range(M):
        if P[i] == X[i]:
            tmp += 1

    if tmp == M:
        ans += 1

print(ans)
