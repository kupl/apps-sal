(K, N) = list(map(int, input().split()))
MAX = K + N + 3
mod = 998244353
fac = [1] * (MAX + 1)
for i in range(1, MAX + 1):
    fac[i] = fac[i - 1] * i % mod
rev_m = [1] * (MAX + 1)
rev_m[MAX] = pow(fac[MAX], mod - 2, mod)
for i in range(MAX, 0, -1):
    rev_m[i - 1] = rev_m[i] * i % mod


def Comb(n, k):
    return fac[n] * rev_m[k] * rev_m[n - k] % mod


def f(n, k, i):
    if i == 2:
        if n < 0 or (k == 1 and n >= 2):
            return 0
        elif n == 0:
            return 1
        else:
            return (Comb(k - 2 + n, n) + Comb(k - 2 + n - 1, n - 1)) % mod
    else:
        Sp = i // 2 - 1
        ans = 0
        for p in range(Sp + 1):
            ans += g(n, k, i, p)
        return ans % mod


def g(n, k, i, p):
    Sp = i // 2 - 1
    if p == 0:
        return f(n - Sp, k - Sp, 2) * pow(2, Sp, mod) % mod
    else:
        return g(n, k - 2 * p, i - 2 * p, 0) * Comb(Sp, p)


ans = []
for i in range(2, K + 2):
    if i % 2 == 0:
        tmp = f(N, K, i)
    ans.append(tmp)
    print(tmp)
ans = ans[::-1]
for i in range(1, K):
    print(ans[i])
