import itertools
import re
import math
import getpass
import sys

debug = False
files = False
if getpass.getuser() == 'frohe':
    debug = True

if debug and files:
    sys.stdin = open('test.in')


def ria():
    return [int(i) for i in input().split()]


ar = ria()
hf=sum(ar)/2
for i in itertools.combinations(ar,3):
    if sum(i)==hf:
        print('YES')
        return
print('NO')
