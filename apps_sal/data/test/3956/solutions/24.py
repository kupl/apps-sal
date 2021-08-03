K, N = map(int, input().split())
mod = 998244353
A = []
p = mod - 2
while p != 0:
    A = [p % 2] + A[:]
    p //= 2


def inved(x):
    y = 1
    for _ in range(len(A)):
        if A[_] == 1:
            y *= x
            y %= mod
        if _ != len(A) - 1:
            y *= y
            y %= mod
    return y


X = [0 for i in range(2 * K - 1)]
frac = [1]
for i in range(N + K):
    frac.append(((i + 1) * frac[i]) % mod)
invf = []
for i in range(N + K + 1):
    invf.append(inved(frac[i]))
for k in range(2, K + 2):
    S = 0
    sign = 1
    l = k // 2
    for m in range(min(l + 1, N // 2 + 1)):
        prod = (sign * (frac[l] * frac[N + K - 2 * m - 1])) % mod
        prod *= (invf[m] * invf[l - m]) % mod
        prod %= mod
        prod *= (invf[N - 2 * m] * invf[K - 1]) % mod
        prod %= mod
        S += prod
        S %= mod
        sign *= -1
    X[k - 2], X[2 * K - k] = S, S
for i in range(2 * K - 1):
    print(X[i])
