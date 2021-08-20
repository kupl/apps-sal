(N, M, K) = list(map(int, input().split()))
A = sorted([int(a) for a in input().split()])[:K][::-1]
B = [0]
for a in A:
    B.append(B[-1] + a)
X = [0] * (K + 1)
for _ in range(M):
    (x, y) = list(map(int, input().split()))
    if x <= K:
        X[x] = max(X[x], y)
Y = [0] * (K + 1)
for i in range(1, K + 1):
    mi = 10 ** 100
    for j in range(1, i + 1):
        s = Y[i - j] + B[i - X[j]] - B[i - j]
        mi = min(mi, s)
    Y[i] = mi
print(Y[K])
