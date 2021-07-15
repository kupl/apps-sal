MOD = 1000000007


def mod_inv(mod, a):
    old_t, t = 0, 1
    old_r, r = mod, a

    while r != 0:
        quotient = old_r // r

        old_r, r = r, old_r - quotient * r
        old_t, t = t, old_t - quotient * t

    return old_t % mod


def combine(n, k, mod):
    if k > n // 2:
        k = n - k
    u = 1
    for i in range(n - k + 1, n + 1):
        u = u * i % mod

    v = 1
    for i in range(1, k + 1):
        v = v * i % mod

    return u * mod_inv(mod, v) % MOD


def main():
    X, Y = list(map(int, input().split()))
    m1 = X + Y
    if m1 % 3 == 0:
        m = m1 // 3
        if X < m or Y < m:
            print((0))
        else:
            print((combine(m, X - m, MOD)))
    else:
        print((0))


def __starting_point():
    main()

__starting_point()
