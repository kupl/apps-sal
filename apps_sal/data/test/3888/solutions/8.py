import sys
input = lambda: sys.stdin.readline().rstrip()
def mex(i, j):
    if i == 0:
        return 2 if j == 1 else 1
    if i == 1:
        return 0 if j else 2
    return 0 if j else 1

ans = [0, 0, 0]
N = int(input())

if N < 10:
    X = [[0] * N for _ in range(N)]
    A = [int(a) for a in input().split()]
    for i, a in enumerate(A):
        X[0][i] = a
        ans[a] += 1
    for i in range(1, N):
        a = int(input())
        X[i][0] = a
        ans[a] += 1
    for i in range(1, N):
        for j in range(1, N):
            a = mex(X[i][j-1], X[i-1][j])
            X[i][j] = a
            ans[a] += 1
    print((*ans))
    return

K = 3
X = [[0] * (N if i <= K else K + 1) for i in range(N)]
A = [int(a) for a in input().split()]
for i, a in enumerate(A):
    X[0][i] = a
    ans[a] += 1
for i in range(1, N):
    a = int(input())
    X[i][0] = a
    ans[a] += 1

for i in range(1, N):
    Xi = X[i]
    Xi1 = X[i-1]
    for j in range(1, K):
        a = mex(Xi[j-1], Xi1[j])
        ans[a] += 1
        X[i][j] = a
for i in range(1, K):
    Xi = X[i]
    Xi1 = X[i-1]
    for j in range(K, N):
        a = mex(Xi[j-1], Xi1[j])
        ans[a] += 1
        X[i][j] = a

for i in range(K, N):
    j = K
    a = mex(X[i][j-1], X[i-1][j])
    X[i][j] = a
    ans[a] += N - i
for j in range(K + 1, N):
    i = K
    a = mex(X[i][j-1], X[i-1][j])
    X[i][j] = a
    ans[a] += N - j

print((*ans))

