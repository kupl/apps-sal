import sys
input = sys.stdin.readline
(N, M) = map(int, input().split())
(MA, lg) = (1 << 19, 20)
A = []
for _ in range(N):
    (l, r) = map(int, input().split())
    A.append([l, r])
X = [[-1] * MA for i in range(lg)]
for i in range(N):
    X[0][A[i][0]] = max(X[0][A[i][0]], A[i][1])
for i in range(1, MA):
    X[0][i] = max(X[0][i], X[0][i - 1])
for k in range(1, lg):
    for i in range(MA):
        a = X[k - 1][i]
        if a >= 0:
            X[k][i] = X[k - 1][a]
for _ in range(M):
    (a, b) = map(int, input().split())
    ans = 1
    for k in range(lg)[::-1]:
        if X[k][a] < b:
            a = X[k][a]
            ans += 2 ** k
    print(-1 if X[0][a] < b or ans > MA else ans)
