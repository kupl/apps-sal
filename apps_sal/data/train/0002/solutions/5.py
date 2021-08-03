from math import *
from bisect import *
from collections import *
from random import *
from decimal import *
import sys
input = sys.stdin.readline


def inp():
    return int(input())


def st():
    return input().rstrip('\n')


def lis():
    return list(map(int, input().split()))


def ma():
    return list(map(int, input().split()))


t = inp()
while(t):
    t -= 1
    n = inp()
    a = lis()
    b = lis()
    c = lis()
    r = [a[0]]
    for i in range(1, n):
        if(i == n - 1):
            if(a[i] != r[0] and a[i] != r[-1]):
                r.append(a[i])
                continue
            if(b[i] != r[0] and b[i] != r[-1]):
                r.append(b[i])
                continue
            if(c[i] != r[0] and c[i] != r[-1]):
                r.append(c[i])
                continue
        if(a[i] != r[-1]):
            r.append(a[i])
            continue
        if(b[i] != r[-1]):
            r.append(b[i])
            continue
        if(c[i] != r[-1]):
            r.append(c[i])
            continue
    print(*r)
