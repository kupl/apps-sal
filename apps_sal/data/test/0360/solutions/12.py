import getpass
import math
import sys
import string
import re
import math
import random
from decimal import Decimal, getcontext


def ria():
    return [int(i) for i in input().split()]


if getpass.getuser() != 'frohenk':
    filename = 'half'
    # sys.stdin = open('input.txt')
    # sys.stdout = open('output.txt', 'w')
else:
    sys.stdin = open('input.txt')
    # sys.stdin.close()

n = ria()[0]
ar = []
for i in range(n):
    ar.append(ria())
lk = ria()[0]
cnt = 0
lk -= 1
for l, r in ar:
    if l <= lk and r <= lk:
        cnt += 1
print(n - cnt)

