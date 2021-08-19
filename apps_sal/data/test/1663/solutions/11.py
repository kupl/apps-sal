import sys
import random
from fractions import Fraction
from math import *


def input():
    return sys.stdin.readline().strip()


def iinput():
    return int(input())


def finput():
    return float(input())


def tinput():
    return input().split()


def linput():
    return list(input())


def rinput():
    return list(map(int, tinput()))


def fiinput():
    return list(map(float, tinput()))


def rlinput():
    return list(map(int, input().split()))


def trinput():
    return tuple(rinput())


def srlinput():
    return sorted(list(map(int, input().split())))


def NOYES(fl):
    if fl:
        print('NO')
    else:
        print('YES')


def YESNO(fl):
    if fl:
        print('YES')
    else:
        print('NO')


def main():
    s = input()
    n = len(s)
    mod = int(1000000000.0) + 7
    q = [0 for i in range(100100)]
    w = [0 for i in range(100100)]
    q[0] = 1
    w[0] = 1
    res = 1
    for i in range(1, 100100):
        res = res * 10 % mod
        q[i] = q[i - 1] + res
        q[i] %= mod
        w[i] = w[i - 1] * 10
        w[i] %= mod
    (l, res, r) = (0, 0, 0)
    for i in range(n - 1):
        l *= 10
        l += int(s[i])
        l %= mod
        res += l * q[n - 2 - i] % mod
        res %= mod
    for i in range(n - 1, 0, -1):
        r += w[n - 1 - i] * int(s[i])
        r %= mod
        res += r * i % mod
        res %= mod
    print(res)


for i in range(1):
    main()
