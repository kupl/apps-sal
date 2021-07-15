import getpass
import sys

if getpass.getuser() != 'frohenk':
    filename = 'half'
    # sys.stdin = open('input.txt')
    # sys.stdout = open('output.txt', 'w')
else:
    sys.stdin = open('input.txt')
    # sys.stdin.close()

import math
import string
import re
import math
import random
from decimal import Decimal, getcontext


def ria():
    return [int(i) for i in input().split()]


n = ria()[0]
st = input()
mn = 10 ** 9
for i in range(len(st) - 3):
    cr = st[i:i + 4]
    crs = 0
    for j in range(4):
        crs += min([abs(ord(cr[j]) - ord('ACTG'[j])-26),abs(ord(cr[j]) - ord('ACTG'[j])+26),abs(ord(cr[j]) - ord('ACTG'[j]))])
    mn = min(mn, crs)
print(mn)

