def main():
    MOD = 10 ** 9 + 7
    S = input()
    (z, a, b, c) = (1, 0, 0, 0)
    for x in S:
        if x == 'C':
            c = (c + b) % MOD
        elif x == 'B':
            b = (b + a) % MOD
        elif x == 'A':
            a = (a + z) % MOD
        elif x == '?':
            (z, a, b, c) = (z * 3 % MOD, (a * 3 + z) % MOD, (b * 3 + a) % MOD, (c * 3 + b) % MOD)
    print(c)


def __starting_point():
    main()


__starting_point()
