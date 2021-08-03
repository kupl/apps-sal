N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
pA = [0] * (N + 1)
for i in range(N):
    pA[i + 1] = pA[i] + A[i]
pB = [0] * (M + 1)
for i in range(M):
    pB[i + 1] = pB[i] + B[i]
ans = 0
for p in range(1, int(K**0.5) + 1):
    if K % p > 0:
        continue
    q = K // p
    if p > q:
        break

    X = 0
    for i in range(N + 1 - p):
        if pA[i + p] - pA[i] == p:
            X += 1
    Y = 0
    for i in range(M + 1 - q):
        if pB[i + q] - pB[i] == q:
            Y += 1
    ans += X * Y
    if p == q:
        break
    X = 0
    for i in range(N + 1 - q):
        if pA[i + q] - pA[i] == q:
            X += 1
    Y = 0
    for i in range(M + 1 - p):
        if pB[i + p] - pB[i] == p:
            Y += 1
    ans += X * Y
print(ans)
