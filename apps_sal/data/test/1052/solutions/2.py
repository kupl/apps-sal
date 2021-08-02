from math import factorial as fac


def binomial(x, y):
    try:
        binom = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binom = 0
    return binom


n, k = [int(i) for i in input().split()]

if k == 1:
    print(1)
elif k == 2:
    print(binomial(n, 2) + 1)
elif k == 3:
    print(binomial(n, 3) * 2 + binomial(n, 2) + 1)
elif k == 4:
    print(binomial(n, 4) * 9 + binomial(n, 3) * 2 + binomial(n, 2) + 1)
