import sys
import string
from math import gcd
import getpass
import math
from decimal import Decimal


def ria():
    return [int(i) for i in input().split()]


if getpass.getuser() != 'frohenk':
    filename = 'half'
    # sys.stdin = open('input.txt')
    # sys.stdout = open('output.txt', 'w')
else:
    sys.stdin = open('input.txt')
    # sys.stdin.close()
# sys.stdout = open('input.txt','w')

n = ria()[0]
x, y = ria()
bx, by = ria()
cx, cy = ria()

x1, y1 = x - bx, y - by
x2, y2 = x - cx, y - cy

if abs(x2) == abs(y2):
    print('NO')
    return
if math.copysign(x2, x1) != x2:
    print('NO')
    return
if math.copysign(y2, y1) != y2:
    print('NO')
    return
print('YES')
