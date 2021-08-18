import itertools
import re
import math
import getpass
import sys
import string

debug = getpass.getuser() == 'frohe'
files = True

if debug and files:
    sys.stdin = open('test.in')
else:
    pass
    # sys.stdin = open('schools.in')
    # sys.stdout = open('schools.out', 'w')


def ria():
    return [int(i) for i in input().split()]


n = ria()[0]
pl = [1, 2]
sp = 3
for i in range(n):
    wn = ria()[0]
    if wn not in pl:
        print('NO')
        return

    pl = [wn] + [sp]
    spn = [1, 2, 3]
    for j in pl:
        spn.remove(j)
    sp = spn[0]
print('YES')
