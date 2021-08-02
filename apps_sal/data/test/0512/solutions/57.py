R, P, I, J = range, print, input, int
n = J(I())
A, C, L = [list(map(J, I().split()))for i in R(n)], [0] * (2 * n), [-1] * (2 * n)
for i, (a, b) in enumerate(A):
    a -= 1; b -= 1
    if a != -2:
        if L[a] >= 0: P("No"); return
        C[a] = 1; L[a] = i
    if b != -2:
        if L[b] >= 0: P("No"); return
        C[b] = -1; L[b] = i


def f(l, r):
    m = (l + r) // 2
    if min(C[l:m]) == -1 or max(C[m:r]) == 1: return 0
    X, Y = L[l:m], L[m:r]
    for i in R(len(X)):
        if X[i] == Y[i]: continue
        elif X[i] != -1 != Y[i]: return 0
        elif (X[i] != -1 and X[i] in Y) or (Y[i] != -1 and Y[i] in X): return 0
    return 1


dp = [0] * (n + 1)
dp[0] = 1
for i in R(n):
    for j in R(i + 1, n + 1):
        if dp[i] * f(i * 2, j * 2): dp[j] = 1
P("NYoe s"[dp[n]::2])
