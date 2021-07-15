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

mod = 10 ** 9 + 7


def ria():
    return [int(i) for i in input().split()]


def alg_s(b, s, n):
    # print(b, b + s * (n - 1))

    return ((b + s * (n - 1) + b) * n // 2) % mod


L, R = ria()
cr1 = 1
cr2 = 2
lk = 1
cr = 1
is1 = True
ans = 0
for j in range(300):
    l = cr
    r = cr + lk - 1

    if is1:
        if l >= L and r <= R:
            ans += alg_s(cr1, 2, r - l + 1)
        elif L >= l and R <= r:
            ans += alg_s(cr1 + (L - l) * 2, 2, R - L + 1)
        elif r >= L >= l:
            ans += alg_s(cr1 + (L - l) * 2, 2, r - L + 1)
            # print('A')
        elif l <= R <= r:
            ans += alg_s(cr1, 2, R - l + 1)
            # print('B')
        cr1 += (r - l + 1) * 2
    else:
        if l >= L and r <= R:
            ans += alg_s(cr2, 2, r - l + 1)
        elif L >= l and R <= r:
            ans += alg_s(cr2 + (L - l) * 2, 2, R - L + 1)
        elif r >= L >= l:
            ans += alg_s(cr2 + (L - l) * 2, 2, r - L + 1)
            # print('C')
        elif l <= R <= r:
            ans += alg_s(cr2, 2, R - l + 1)
            # print('D')

        cr2 += (r - l + 1) * 2

    is1 = not is1
    cr += cr
    lk *= 2
    ans %= mod
print(ans)

