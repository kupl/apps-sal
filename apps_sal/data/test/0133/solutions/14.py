import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return map(int, minp().split())


mod = int(1000000000.0 + 7)
(n, m) = mints()
print(pow((pow(2, m, mod) + mod - 1) % mod, n, mod))
