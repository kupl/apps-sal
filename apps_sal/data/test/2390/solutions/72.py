(N, C) = list(map(int, input().split()))
D = [[int(x) for x in input().split()] for _ in range(N)]
(X, V, M) = ([0] * (N + 1), [0] * (N + 1), [0] * (N + 1))
for i in range(1, N + 1):
    (X[i], V[i]) = (D[i - 1][0], V[i - 1] + D[i - 1][1])
    M[i] = M[i - 1] if M[i - 1] > V[i] - D[i - 1][0] else V[i] - D[i - 1][0]
m = 0
for i in range(1, N + 1):
    e = M[i - 1] - (C - X[i]) if M[i - 1] > C - X[i] else 0
    e += V[N] - V[i - 1] - (C - X[i])
    m = m if m > e else e
M = [0] * (N + 2)
for i in range(N, 0, -1):
    p = V[N] - V[i - 1] - (C - X[i])
    M[i] = M[i + 1] if M[i + 1] > p else p
for i in range(1, N + 1):
    e = M[i + 1] - X[i] if M[i + 1] > X[i] else 0
    e += V[i] - X[i]
    m = m if m > e else e
print(m)
