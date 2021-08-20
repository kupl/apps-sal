import copy
import fractions
import itertools
import numbers
import string
import sys


def powmod(x, p, m):
    if p <= 0:
        return 1
    if p <= 1:
        return x % m
    return powmod(x * x % m, p // 2, m) * (x % m) ** (p % 2) % m


def to_basex(num, x):
    while num > 0:
        yield (num % x)
        num //= x


def from_basex(it, x):
    ret = 0
    p = 1
    for d in it:
        ret += d * p
        p *= x
    return ret


def core():
    (n, m) = (int(x) for x in input().split())
    a = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    s = [(c[i], i) for i in range(n)]
    s.sort(reverse=True)
    for _ in range(m):
        if not s:
            print(0)
        else:
            (tj, dj) = (int(x) for x in input().split())
            tj -= 1
            if a[tj] >= dj:
                print(dj * c[tj])
                a[tj] -= dj
            else:
                bill = a[tj] * c[tj]
                dj -= a[tj]
                a[tj] = 0
                while dj > 0:
                    if not s:
                        bill = 0
                        break
                    if a[s[-1][1]] == 0:
                        _ = s.pop()
                    elif a[s[-1][1]] >= dj:
                        bill += dj * c[s[-1][1]]
                        a[s[-1][1]] -= dj
                        dj = 0
                    else:
                        bill += a[s[-1][1]] * c[s[-1][1]]
                        dj -= a[s[-1][1]]
                        a[s[-1][1]] = 0
                        _ = s.pop()
                print(bill)


core()
