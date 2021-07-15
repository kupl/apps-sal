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

    print((comb_mod(a+b, a, 10 ** 9 + 7)))


def comb_mod(n, k, p):
    def fact_mod(x, p):
        v = 1
        for i in range(1, x+1):
            v *= i
            v %= p
        return v

    # n! mod p
    n_mod = fact_mod(n, p)
    # k!^(p-2) mod p
    k_mod = pow(fact_mod(k, p), p-2, p)
    # (n-k)!^(p-2) mod p
    n_minus_k_mod = pow(fact_mod(n-k, p), p-2, p)

    return (n_mod * k_mod * n_minus_k_mod) % p


def __starting_point():
    main()

__starting_point()
