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
else:
    sys.stdin = open('input.txt')
(n, k) = ria()
rcks = n + 1
mny = n
mvs = min((k - 1) * 2 + (n - k), k - 1 + (n - k) * 2)
if k == 1:
    mvs = n - 1
if k == n:
    mvs = n - 1
print(mvs + rcks + mny)
