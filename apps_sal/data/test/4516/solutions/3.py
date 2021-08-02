N, M = map(int, input().split())
*X, = map(int, input().split())
for i in range(M):
    X[i] -= 1

R = 0
S = [0] * N
T = [0] * N
D = [0] * (N + 1)
for i in range(M - 1):
    if X[i] < X[i + 1]:
        D[X[i] + 1] += 1
        D[X[i + 1]] -= 1
    elif X[i] > X[i + 1]:
        D[X[i + 1] + 1] += 1
        D[X[i]] -= 1

    d = abs(X[i] - X[i + 1])
    S[X[i]] += d
    S[X[i + 1]] += d
    if X[i] < X[i + 1]:
        T[X[i]] += X[i + 1]
        T[X[i + 1]] += X[i] + 1
    elif X[i] > X[i + 1]:
        T[X[i]] += X[i + 1] + 1
        T[X[i + 1]] += X[i]
    R += d
for i in range(N - 1):
    D[i + 1] += D[i]
ans = [0] * N
for i in range(N):
    ans[i] = R + T[i] - S[i] - D[i]
print(*ans)
