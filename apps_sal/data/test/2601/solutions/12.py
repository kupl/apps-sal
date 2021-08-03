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


t = int(input())
while(t):
    t -= 1
    n = inp()
    a = lis()
    fl = 0
    for i in range(n - 1):
        if(a[i] > a[i + 1]):
            fl += 1
            continue
    if(fl == n - 1):
        print("NO")
    else:
        print("YES")
