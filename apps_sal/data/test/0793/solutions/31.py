import sys
from math import ceil


def input():
    return sys.stdin.readline().strip()


def iinput():
    return int(input())


def finput():
    return float(input())


def tinput():
    return input().split()


def rinput():
    return map(int, tinput())


def rlinput():
    return list(rinput())


def nok(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


def main():
    mod = 1000000000.0 + 7
    (n, m) = rinput()
    s = rlinput()
    t = rlinput()
    a = [1] * (m + 1)
    for j in s:
        d = a[:]
        k = 0
        for (i, v) in enumerate(t):
            d[i] = (k + d[i]) % mod
            if j == v:
                k = (k + a[i]) % mod
        d[-1] = (k + d[-1]) % mod
        a = d[:]
    print(int(a[-1]))


main()
