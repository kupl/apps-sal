import sys
import string
from math import gcd
import getpass
import math
from decimal import Decimal
import pprint


def ria():
    return [int(i) for i in input().split()]


if getpass.getuser() != 'frohenk':
    filename = 'half'
    # sys.stdin = open('input.txt')
    # sys.stdout = open('output.txt', 'w')
else:
    sys.stdin = open('input.txt')
    # sys.stdin.close()
# sys.stdout = open('output.txt', 'w')


n = ria()[0]
x, y = ria()
d1 = abs(1 - x) + abs(1 - y)
d2 = abs(n - x) + abs(n - y)
if d1 <= d2:
    print('White')
else:
    print('Black')
