from collections import defaultdict
import math


MOD = 998244353


def facmod(n):
    fac = 1
    for i in range(2, n + 1):
        fac *= i
        fac %= MOD
    return fac


def main():
    n = int(input())
    s = [tuple(int(s) for s in input().split()) for _ in range(n)]

    count = defaultdict(int)

    for a, _ in s:
        count[a] += 1

    first = 1
    for c in list(count.values()):
        first *= facmod(c)
        first %= MOD

    count = defaultdict(int)

    for _, b in s:
        count[b] += 1

    second = 1
    for c in list(count.values()):
        second *= facmod(c)
        second %= MOD

    count = defaultdict(int)

    for t in s:
        count[t] += 1

    both = 1
    for c in list(count.values()):
        both *= facmod(c)
        both %= MOD

    s.sort()

    for i, (_, b) in enumerate(s[:-1]):
        if b > s[i + 1][1]:
            both = 0
            break

    print((facmod(n) - (first + second - both)) % MOD)


def __starting_point():
    main()


__starting_point()
