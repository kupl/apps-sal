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


n, m = ria()
st = input()

for i in range(m):
    l, r, a, b = input().split()
    l = int(l)
    r = int(r)
    l -= 1
    st = st[:l] + st[l:r].replace(a, b) + st[r:]
print(st)
