from math import gcd
from collections import Counter
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

MOD = 10**9 + 7


def main():
    N, *ab = list(map(int, read().split()))

    ab_zero = 0
    ratio = []
    for a, b in zip(*[iter(ab)] * 2):
        if a == 0 and b == 0:
            ab_zero += 1
        else:
            if b < 0:
                a, b = -a, -b
            if b == 0:
                a = 1
            g = gcd(a, b)
            a //= g
            b //= g
            ratio.append((a, b))

    s = Counter(ratio)

    bad = 1
    no_pair = 0
    for k, v in list(s.items()):
        a, b = k
        if a > 0:
            if (-b, a) in s:
                bad *= pow(2, v, MOD) + pow(2, s[(-b, a)], MOD) - 1
                bad %= MOD
            else:
                no_pair += v

        elif (b, -a) not in s:
            no_pair += v

    bad *= pow(2, no_pair, MOD)
    bad %= MOD

    ans = (bad + ab_zero - 1) % MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
