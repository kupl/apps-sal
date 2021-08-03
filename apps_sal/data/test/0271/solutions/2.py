import math
import sys
import getpass
import bisect


def ria():
    return [int(i) for i in input().split()]


files = False

if getpass.getuser().lower() == 'frohe' and files:
    sys.stdin = open('test.in')
    # sys.stdout = open('test.out', 'w')

n = ria()[0]
print(int(round(n / 10) * 10))
