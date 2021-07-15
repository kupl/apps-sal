def main():
    MOD = 10 ** 9 + 7

    s = input()

    x, a, b, c = 1, 0, 0, 0

    for char in s:
        if char == 'A':
            a = (a + x) % MOD
        elif char == 'B':
            b = (b + a) % MOD
        elif char == 'C':
            c = (c + b) % MOD
        else:
            x, a, b, c = 3 * x % MOD, (3 * a + x) % MOD, (3 * b + a) % MOD, (3 * c + b) % MOD

    print(c)


def __starting_point():
    main()

__starting_point()
