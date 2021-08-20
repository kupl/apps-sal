import collections
from math import gcd
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    c = collections.Counter()
    mod = 10 ** 9 + 7
    for _ in range(n):
        (a, b) = list(map(int, input().split()))
        g = abs(gcd(a, b))
        if g == 0:
            g = 1
        a //= g
        b //= g
        c[a, b] += 1
    ans = 1
    s = set()
    for (i, j) in c:
        if (i, j) == (0, 0):
            continue
        if (i, j) not in s:
            s.add((i, j))
            s.add((-i, -j))
            s.add((-j, i))
            s.add((j, -i))
            ans *= (pow(2, c[i, j] + c[-i, -j], mod) + pow(2, c[j, -i] + c[-j, i], mod) - 1) % mod
    print((ans - 1 + c[0, 0]) % mod)


def __starting_point():
    main()


__starting_point()
