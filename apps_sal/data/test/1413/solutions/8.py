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
rs = 0
for i in range(n):
    if int(st[i]) % 2 == 0:
        rs += i + 1
print(rs)
