import sys
import math
MOD = 1000000007


def inv(a, b):
    if a > 1:
        return b - inv(b % a, a) * b // a
    else:
        return 1


def main():
    n = int(sys.stdin.readline().strip())
    t = 1
    m = 1
    for i in range(1, n + 2):
        t = t * (n + i + 1) % MOD
        m = m * i % MOD
    print(t * inv(m, MOD) % MOD - 1)


def __starting_point():
    main()


__starting_point()
