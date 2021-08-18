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

n = ria()[0]
if n == 1:
    print(1)
    return

if n == 2:
    print(1, 2)
    return

if n == 3:
    print(1, 1, 3)
    return

ar = [0] * 30

for i in range(30):
    ar[i] = n // (2 ** i) - n // (2 ** (i + 1))
sd = 0
for i in range(30):
    if sd == n - 1:
        if n == (2**i):
            print(2**i)
        else:
            print(n - n % (2**(i - 1)))
        return
    for j in range(ar[i]):
        print(2 ** i, end=' ')
        sd += 1
