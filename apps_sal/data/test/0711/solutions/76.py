def prime_factor(n):
    if n == 1:
        return [[1, 0]]
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


MOD = 10 ** 9 + 7
lim = 200000
inv_t = [-1 for i in range(lim + 1)]
factrial = [-1 for i in range(lim + 1)]
factrial_inv = [-1 for i in range(lim + 1)]


def set_inv(max=lim):
    inv_t[0] = 0
    for i in range(1, max):
        inv_t[i] == mod_inv(i)


def mod_inv(x, mod=MOD):
    (y, u, v, _x) = (mod, 1, 0, x)
    while y:
        t = _x // y
        _x -= t * y
        (_x, y) = (y, _x)
        u -= t * v
        (u, v) = (v, u)
    u %= mod
    if u < 0:
        u += mod
    return u


def mod_pow(a, n, mod=MOD):
    res = 1
    while n:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res


def set_factrial(max=lim, mod=MOD):
    c = 1
    factrial[0] = factrial_inv[0] = 1
    for i in range(1, max):
        c *= i
        c %= mod
        factrial[i] = c
        factrial_inv[i] = mod_inv(c, mod)


def comb(a, b, mod=MOD):
    if factrial[0] == -1:
        set_factrial()
    return factrial[a] * factrial_inv[b] * factrial_inv[a - b] % mod


(n, m) = [int(_) for _ in input().split()]
ans = 1
for (p, e) in prime_factor(m):
    ans *= comb(n - 1 + e, e)
    ans %= MOD
print(ans)
