from math import gcd


def factor(x):
    factors = set()

    f = 2

    while f * f <= x:
        while x % f == 0:
            factors.add(f)
            x //= f

        f += 1

    if x > 1:
        factors.add(x)

    return factors


for _ in range(int(input())):
    a, m = map(int, input().split())

    g = gcd(a, m)

    a //= g
    m //= g

    # now just find such that 0 <= x < m & gcd(a + x, m) = 1
    # how many numbers in [a, a + m) are coprime to m

    f = list(factor(m))

    tot = 0

    for i in range(1, 2 ** len(f)):
        mul = 1

        bc = -1

        for j in range(len(f)):
            if i & (1 << j):
                mul *= f[j]
                bc = -bc

        tot += bc * (m // mul + (a % mul < (a + m - 1) % mul))

    print(m - tot)
