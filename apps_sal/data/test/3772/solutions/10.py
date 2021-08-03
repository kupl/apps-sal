import fractions


def resistance():
    #  print("Input the two values")
    _a, _b = input().split()
    a = int(_a)
    b = int(_b)
    answer = 1
    f = fractions.Fraction(a, b)
    one = fractions.Fraction(1, 1)

    while (f != one):
        n = f.numerator
        d = f.denominator

        #  If either the num or denom are one, go straight up the line and finish
        if (n == 1) and (d == 1):
            print(answer)
            return
        if (n == 1):
            print(answer + d - 1)
            return
        if (d == 1):
            print(answer + n - 1)
            return

        if (f > 1):
            q = n // d
            n = n - q * d
            f = fractions.Fraction(n, d)
            answer = answer + q
        else:
            nbound = (1 - f) / f
            n = nbound.numerator
            d = nbound.denominator
            then = n // d + 1
            answer = answer + then
            f = f / (1 - then * f)

    print(answer)


resistance()
