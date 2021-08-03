
def main():
    import fractions

    a, b, c, d = [int(i) for i in input().split()]

    d_c = b // c - (a - 1) // c
    d_d = b // d - (a - 1) // d

    cd = c * d // fractions.gcd(c, d)
    d_cd = b // cd - (a - 1) // cd

    print((b - a + 1 - (d_c + d_d - d_cd)))


def __starting_point():
    main()


__starting_point()
