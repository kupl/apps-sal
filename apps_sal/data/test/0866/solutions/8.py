MOD = 10 ** 9 + 7


def main():
    X, Y = list(map(int, input().split()))
    if (2 * X - Y) % 3 == 0 and (2 * Y - X) % 3 == 0:
        a = (2 * X - Y) // 3
        b = (2 * Y - X) // 3
    else:
        print((0))
        return
    if a < 0 or b < 0:
        print((0))
        return

    # (a+b)! % MOD
    ab_mod = fact_mod(a + b)
    # (a!)^(MOD-2) % MOD
    a_mod = pow(fact_mod(a), MOD - 2, MOD)
    # (b!)^(MOD-2) % MOD
    b_mod = pow(fact_mod(b), MOD - 2, MOD)
    print(((ab_mod * a_mod * b_mod) % MOD))


def fact_mod(x):
    v = 1
    for i in range(1, x + 1):
        v *= i
        v %= MOD
    return v


def __starting_point():
    main()


__starting_point()
