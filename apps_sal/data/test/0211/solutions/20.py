MOD = 1000000009


def log_mult(a, p):
    if p == 0:
        return 1
    else:
        z = log_mult(a, p // 2)
        z = z * z % MOD
        if p % 2 == 1:
            return a * z % MOD
        else:
            return z


def log_iterative(a, p):
    res = 1
    while p > 0:
        if p % 2 == 1:
            res = res * a % MOD
        a = a * a % MOD
        p //= 2
    return res


(n, m, k) = list(map(int, input().split()))
c = n // k * (k - 1) + n % k
if c >= m:
    print(m)
else:
    d = m - c
    res = log_iterative(2, d + 1) - 2
    res = res * k % MOD
    print((res + m - d * k) % MOD)
