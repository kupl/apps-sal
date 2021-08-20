from functools import reduce


def main():
    n = int(input())
    if n == 1:
        print(1, 0)
        return
    fact = dict()
    d = 2
    c = 0
    while n % d == 0:
        c += 1
        n //= d
    if c > 0:
        fact[d] = c
    d = 3
    while n != 1:
        c = 0
        while n % d == 0:
            c += 1
            n //= d
        if c > 0:
            fact[d] = c
        d += 2
    ans = reduce(lambda x, y: x * y, fact.keys())
    maxPow = max(fact.values())
    x = 0
    while maxPow > 1 << x:
        x += 1
    if maxPow == 1 << x and all([y == maxPow for y in fact.values()]):
        print(ans, x)
        return
    else:
        print(ans, x + 1)
        return


def __starting_point():
    main()


__starting_point()
