MOD = int(1e9) + 7


def fact(x):
    k = 1
    for i in range(1, x + 1):
        k = (k * i) % MOD
    return k


def inverse(b):
    r = 1
    e = MOD - 2
    while e:
        if e % 2 == 1:
            r = (r * b) % MOD
        b = (b * b) % MOD
        e >>= 1
    return r


def comb(i, j):
    if i == 0 or j == 0:
        return 0
    num = fact(i + j)
    num *= inverse(fact(i))
    num %= MOD
    num *= inverse(fact(j))
    num %= MOD
    return num


rc = list(map(int, input().split()))
ans = 0
ans += comb(rc[2] + 1, rc[3] + 1)
ans -= comb(rc[0], rc[3] + 1)
ans -= comb(rc[2] + 1, rc[1])
ans += comb(rc[0], rc[1])
ans += MOD
ans += MOD
ans %= MOD
print(ans)
