def read_int():
    return int(input())


def read_ints():
    return list(map(int, input().split(' ')))


fac = [1]
rev = []
mod = 998244353


def fexp(x, y):
    ans = 1
    while y > 0:
        if y % 2 == 1:
            ans = ans * x % mod
        x = x * x % mod
        y //= 2
    return ans


def comb(n, k):
    return fac[n] * rev[k] * rev[n - k] % mod


(n, k) = read_ints()
if k >= n:
    print(0)
else:
    for i in range(1, n + 5):
        fac.append(fac[-1] * i % mod)
    for i in range(n + 5):
        rev.append(fexp(fac[i], mod - 2))
    if k == 0:
        print(fac[n])
    else:
        ways = comb(n, k)
        col = 0
        for i in range(n - k):
            sign = 1 if i % 2 == 0 else -1
            col += sign * comb(n - k, i) * fexp(n - k - i, n)
            col %= mod
            if col < 0:
                col += mod
        print(ways * col * 2 % mod)
