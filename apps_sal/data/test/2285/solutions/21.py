import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def do(s):
    r = []
    for i in s.split(':'):
        r.append('0' * (4 - len(i)) + i)
    return ':'.join(r)


n = mint()
for i in range(n):
    s = minp()
    m = s.find('::')
    if m != -1:
        print(do(s[:m]) + ':0000' * (8 - s.count(':')) + ':' + do(s[m + 2:]))
    else:
        print(do(s))
