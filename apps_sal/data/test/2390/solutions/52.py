N, C = map(int, input().split())
X = []
V = []
for _ in range(N):
    x, v = map(int, input().split())
    X.append(x)
    V.append(v)

A = V[:]
B = V[::-1]

for i in range(N - 1):
    A[i + 1] += A[i]
    B[i + 1] += B[i]

P = [0]
Q = [0]

for i in range(N):
    P.append(max(P[-1], A[i] - X[i] * 2))
    Q.append(max(Q[-1], B[i] - (C - X[N - i - 1]) * 2))

ans = 0

for i in range(N):
    ans = max(ans, A[i] + Q[N - i - 1] - X[i])
    ans = max(ans, B[i] + P[N - i - 1] - (C - X[N - i - 1]))

print(ans)
