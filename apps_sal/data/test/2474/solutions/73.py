
def pow2(n, mod):
    """2のn乗まで"""
    t = 1
    yield t
    for _ in range(n):
        t = t * 2 % mod
        yield t


def main():
    MOD = 10 ** 9 + 7

    N = int(input())
    *c, = list(map(int, input().split()))

    c.sort()

    *two, = pow2(N, MOD)

    ans = 0
    for l, x in enumerate(c):
        r = N - l - 1

        t = two[r]
        if r != 0:
            t = (t + two[r - 1] * r) % MOD
        t = t * two[l] % MOD
        t = t * x % MOD
        ans = (ans + t) % MOD

    ans = ans * two[N] % MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
