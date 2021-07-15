import getpass
import sys
import math
from decimal import Decimal
import decimal

files = True
debug = False

if getpass.getuser() == 'frohenk' and files:
    debug = True
    sys.stdin = open("test.in")
    # sys.stdout = open('test.out', 'w')
elif files:
    # fname = "gift"
    # sys.stdin = open("%s.in" % fname)
    # sys.stdout = open('%s.out' % fname, 'w')
    pass


def lcm(a, b):
    return a * b // math.gcd(a, b)


def ria():
    return [int(i) for i in input().split()]


def range_sum(a, b):
    ass = (((b - a + 1) // 2) * (a + b))
    if (a - b) % 2 == 0:
        ass += (b - a + 2) // 2
    return ass


def comba(n, x):
    return (math.factorial(n) // math.factorial(n - x)) // math.factorial(x)


mp = {}
st = input()
for i in st:
    mp[i] = 0
for i in st:
    mp[i] += 1

if len(mp) == 4:
    print('Yes')
    return

if len(mp) == 1:
    print('No')
    return

if len(mp) == 2:
    if min(mp.values()) >= 2:
        print('Yes')
        return

if len(mp) == 3:
    if max(mp.values()) >= 2:
        print('Yes')
        return
print('No')


