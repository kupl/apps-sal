from collections import Counter
import sys
import math
from functools import cmp_to_key
sys.setrecursionlimit(10 ** 6)
mod = 1000000007
inf = int(1e+18)


def main():
    n = int(input())
    p = [tuple(map(int, input().split())) for i in range(n)]
    a = {}
    b = {}
    c = 0
    for (x, y) in p:
        if x == y == 0:
            c += 1
            continue
        if y == 0:
            a[0, 1] = a.get((0, 1), 0) + 1
            continue
        if x == 0:
            b[0, 1] = b.get((0, 1), 0) + 1
        g = math.gcd(x, y)
        if x * y > 0:
            x = abs(x)
            y = abs(y)
            a[x // g, y // g] = a.get((x // g, y // g), 0) + 1
        else:
            x = abs(x)
            y = abs(y)
            b[y // g, x // g] = b.get((y // g, x // g), 0) + 1
    ans = 1
    s = 0
    for (k, v) in list(a.items()):
        if k in b:
            s += v + b[k]
            ans *= pow(2, v) + pow(2, b[k]) - 1
            ans %= mod
    ans *= pow(2, n - s - c, mod)
    print((ans - 1 + c) % mod)


main()
