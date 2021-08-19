import sys
input = sys.stdin.readline
mod = 998244353


def frac(limit):
    frac = [1] * limit
    for i in range(2, limit):
        frac[i] = i * frac[i - 1] % mod
    fraci = [None] * limit
    fraci[-1] = pow(frac[-1], mod - 2, mod)
    for i in range(-2, -limit - 1, -1):
        fraci[i] = fraci[i + 1] * (limit + i + 1) % mod
    return (frac, fraci)


def mul(a, b):
    return a % mod * (b % mod) % mod


def div(a, b):
    return mul(a, pow(b, mod - 2, mod))


(N, M) = list(map(int, input().split()))
X = list(map(int, input().split()))
t = []
for i in range(N):
    t.append((0, X[i]))
Q = []
for i in range(M):
    (a, b) = list(map(int, input().split()))
    Q.append((a, b))
    t.append((1, b))
Y = [0] * (N + M)
Z = [0] * (N + M)
t.sort(key=lambda x: x[1])
d = dict()
d2 = [0] * (N + M)
cnt = 0
for (l, x) in t:
    if x not in d:
        cnt += 1
        d[x] = cnt
        d2[cnt] = x
    if not l:
        Y[cnt] += 1
for i in range(N + M):
    Z[i] = Y[i] * d2[i]
Y.append(0)
Z.append(0)
for i in range(N + M - 1, -1, -1):
    Y[i] = Y[i + 1] + Y[i]
    Z[i] = Z[i + 1] + Z[i]
for (a, b) in Q:
    k = Y[d[b]]
    R = 0
    if k > a:
        R += div(k - a, k) * Z[d[b]]
    if k + 1 > a:
        R += div(k + 1 - a, k + 1) * (Z[0] - Z[d[b]])
    print(R % mod)
