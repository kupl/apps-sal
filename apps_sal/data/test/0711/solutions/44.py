MOD = 10**9 + 7
n, m = list(map(int, input().split()))


def factorization(n):
    retval = []
    tmp = n
    for i in range(2, int(-(-n**.5 // 1)) + 1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            retval.append((i, cnt))
    if tmp != 1:
        retval.append((tmp, 1))
    return retval


def com(n, r):
    X = Y = 1
    if n - r < r:
        r = n - r
    for i in range(1, r + 1):
        Y = Y * i % MOD
        X = X * (n - i + 1) % MOD
    Y = pow(Y, MOD - 2, MOD)
    return X * Y


fact = factorization(m)
ans = 1
for x, p in fact:
    ans *= com(n + p - 1, n - 1)
print((ans % MOD))
