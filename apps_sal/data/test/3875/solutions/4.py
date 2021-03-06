import itertools
P = 10 ** 9 + 7
fainv = [1, 1, 500000004, 166666668, 41666667, 808333339, 301388891]


def C(a, b):
    s = 1
    for i in range(b):
        s = s * (a - i) % P
    return s * fainv[b] % P


def calc(LL):
    L = LL[:]
    K = len(L)
    for i in range(K - 1)[::-1]:
        L[i] = min(L[i], L[i + 1])
    for i in range(1, K)[::-1]:
        L[i] -= L[i - 1]
    X = [0] * K
    f = 1
    re = 0
    cnt = 0
    while f:
        for (x1, x2) in zip(X, X[1:]):
            if x1 > x2:
                break
        else:
            Y = [0] * K
            for x in X:
                Y[x] += 1
            t = 1
            for (j, y) in enumerate(Y):
                t = t * C(L[j], y) % P
            re += t
        cnt += 1
        X[0] += 1
        i = 0
        while X[i] == i + 1:
            X[i] = 0
            i += 1
            if i >= K:
                f = 0
                break
            X[i] += 1
    return re


N = int(input())
Q = list(itertools.permutations(range(N)))
A = [int(a) for a in input().split()]


def LIS(l):
    n = len(l)
    X = [-1] + [n] * n
    for a in l:
        for i in range(n, -1, -1):
            if X[i] < a:
                X[i + 1] = a
                break
    for i in range(n, -1, -1):
        if X[i] < n:
            return i


ans = 0
chk = 0
for q in Q:
    L = []
    s = 0
    for i in range(N):
        if i and q[i - 1] >= q[i]:
            s += 1
        L.append(A[q[i]] + s)
    calcL = calc(L)
    LISq = LIS(q)
    chk += calcL
    ans += calcL * LISq
    if ans >= P:
        ans -= P
s = 1
for a in A:
    s = s * a % P
ans = ans * pow(s, P - 2, P) % P
print(ans)
