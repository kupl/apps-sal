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


n, s = ria()
s -= 1
ar1 = ria()
ar2 = ria()
if ar1[0] == 0:
    print('NO')
    return

if ar1[s] == 1:
    print('YES')
    return
if ar2[s] == 1:
    for i in range(s, n):
        if ar2[i] == 1 and ar1[i] == 1:
            print('YES')
            return
print('NO')
