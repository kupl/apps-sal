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
else:
    sys.stdin = open('input.txt')
n = ria()[0]
for i in range(n):
    print(2 ** str(bin(int(input()))).count('1'))
