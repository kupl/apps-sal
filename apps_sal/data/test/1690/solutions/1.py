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
ar = [i for i in reversed(ria())]
p = ar[0]
sm = ar[0]
for i in range(1,n):
    cr=min(max(0,p-1),ar[i])
    # print(cr)
    p=cr
    sm+=cr
print(sm)
