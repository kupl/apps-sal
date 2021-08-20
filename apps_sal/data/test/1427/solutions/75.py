import sys
from functools import reduce
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


mod = 10 ** 9 + 7


def prime(x):
    pf = defaultdict(int)
    for i in range(2, int(x ** 0.5) + 1):
        while x % i == 0:
            pf[i] += 1
            x //= i
    if x > 1:
        pf[x] = 1
    return pf


def lcm(x, y):
    xx = x.copy()
    yy = y.copy()
    for (k, v) in yy.items():
        xx[k] = max(xx[k], v)
    return xx


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a2 = list(map(prime, a))
    lcms = reduce(lcm, a2)
    lcmss = 1
    for (k, v) in lcms.items():
        lcmss = lcmss * k ** v % mod
    ans = 0
    for aa in a:
        ans += lcmss * pow(aa, -1, mod)
    print(ans % mod)


def __starting_point():
    main()


__starting_point()
