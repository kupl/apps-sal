import math
import re
import string


def ria():
    return [int(i) for i in input().split()]


def ri():
    return int(input())


def rfa():
    return [float(i) for i in input().split()]


eps = 1e-9


def is_equal(a, b):
    return abs(a - b) <= eps


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)


N = ri()
hid = input()
mpk = {}
totalKek = 0
for n, i in enumerate(string.ascii_lowercase):
    mpk[i] = 1 << n
    totalKek |= mpk[i]

M = ri()
revealed = 0
for i in hid:
    if i != '*':
        revealed |= mpk[i]
isAny = False

for i in range(M):
    t = input()
    isAny=True
    bad = False
    hidBit = 0

    for n, j in enumerate(t):
        if hid[n] != '*':
            if hid[n] != t[n]:
                bad = True
            continue


        hidBit |= mpk[j]
    if hidBit & revealed != 0 or bad:
        continue
    totalKek &= hidBit

if isAny:
    print(str(bin(totalKek)).count('1'))
else:
    exit(-1)
