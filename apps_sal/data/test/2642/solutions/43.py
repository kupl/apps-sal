from collections import Counter


def gcd(a, b):
    while b: a, b = b, a % b
    return abs(a)


MOD = 1000000007

# 2 WA


def main():
    N = int(input())
    d = {}
    d[(1, 0)] = (0, 0)
    z = 0
    for i in range(N):
        a, b = (int(x) for x in input().split())
        g = gcd(a, b)
        if g != 0:
            a = a // g
            b = b // g
            if a * b < 0: a = -abs(a)
            elif a * b > 0: a = abs(a)
        b = abs(b)

        if a * b == 0:
            if a == b == 0: z += 1
            elif b == 0: d[(1, 0)] = (d[(1, 0)][0] + 1, d[(1, 0)][1])
            elif a == 0: d[(1, 0)] = (d[(1, 0)][0], d[(1, 0)][1] + 1)
        else:
            if (a, b) in d: d[(a, b)] = (d[(a, b)][0] + 1, d[(a, b)][1])
            elif (b, -a) in d: d[(b, -a)] = (d[(b, -a)][0], d[(b, -a)][1] + 1)
            elif (-b, a) in d: d[(-b, a)] = (d[(-b, a)][0], d[(-b, a)][1] + 1)
            else: d[(a, b)] = (1, 0)

    ans = 1
    for i, j in list(d.values()):
        ans *= (pow(2, i, MOD) + pow(2, j, MOD) - 1)
        ans %= MOD

    print(((ans - 1 + z) % MOD))


def __starting_point():
    main()


__starting_point()
