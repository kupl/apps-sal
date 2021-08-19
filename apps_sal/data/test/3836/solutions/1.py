import math as ma
import sys
from decimal import Decimal as dec
from itertools import permutations


def li():
    return list(map(int, input().split()))


def num():
    return list(map(int, input().split()))


def nu():
    return int(input())


def find_gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


n = nu()
al = []
bo = []
to = []
ze = []
for i in range(n):
    (x, y) = input().split()
    if x == '00':
        ze.append(int(y))
    if x == '11':
        to.append(int(y))
    if x == '10':
        al.append(int(y))
    if x == '01':
        bo.append(int(y))
al.sort(reverse=True)
bo.sort(reverse=True)
to.sort(reverse=True)
ze.sort(reverse=True)
zz = 0
if len(al) <= len(bo):
    zz = sum(al) + sum(bo[0:len(al)])
    gh = bo[len(al):] + ze
    zz = zz + sum(to)
    gh.sort(reverse=True)
    cc = 0
    for i in range(len(gh)):
        if cc == len(to):
            break
        zz += gh[i]
        cc += 1
    print(zz)
else:
    zz = sum(bo) + sum(al[0:len(bo)])
    gh = al[len(bo):] + ze
    zz = zz + sum(to)
    gh.sort(reverse=True)
    cc = 0
    for i in range(len(gh)):
        if cc == len(to):
            break
        zz += gh[i]
        cc += 1
    print(zz)
