import copy
import fractions
import itertools
import string
import sys


def powmod(x, p, m):
    if p <= 0:
        return 1
    if p <= 1:
        return x % m
    return powmod(x * x % m, p // 2, m) * (x % m)**(p % 2) % m


def to_basex(num, x):
    while num > 0:
        yield num % x
        num //= x


def from_basex(it, x):
    ret = 0
    p = 1
    for d in it:
        ret += d * p
        p *= x
    return ret


def core():
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    s = input()

    groups = []
    last_ch = None
    for i in range(len(s)):
        ch = s[i]
        if ch != last_ch:
            groups.append([])
        groups[-1].append(a[i])
        last_ch = ch

    ans = 0
    for g in groups:
        g.sort()
        ans += sum(g[-k:])

    print(ans)


core()
