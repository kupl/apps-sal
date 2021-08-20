import re
import inspect
from sys import argv, exit


def rstr():
    return input()


def rint():
    return int(input())


def rints(splitchar=' '):
    return [int(i) for i in input().split(splitchar)]


def varnames(obj, namespace=globals()):
    return [name for name in namespace if namespace[name] is obj]


def pvar(var, override=False):
    prnt(varnames(var), var, override=override)


def prnt(*args, override=False):
    if '-v' in argv or override:
        print(*args)


def get_qi(p, i, n, F):
    if n // i % 2 == 1:
        return p ^ F[i - 1] ^ F[n % i]
    else:
        return p ^ F[n % i]


def __starting_point():
    n = rint()
    p = rints()
    F = [0 for i in range(n)]
    for i in range(1, n):
        F[i] = F[i - 1] ^ i
    qs = [get_qi(p, i + 1, n, F) for (i, p) in enumerate(p)]
    Q = None
    for q in qs:
        if Q is None:
            Q = q
        else:
            Q ^= q
    print(Q)


__starting_point()
