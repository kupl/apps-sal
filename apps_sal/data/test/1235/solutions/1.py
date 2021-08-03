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
import random
from decimal import Decimal, getcontext
from collections import deque

mod = 10 ** 9 + 7


def ria():
    return [int(i) for i in input().split()]


n = ria()[0]
a = max(ria())
n = ria()[0]
b = max(ria())
print(a, b)
