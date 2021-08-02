from math import *
from bisect import *
from collections import *
from random import *
from decimal import *
from itertools import *
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
    x = n % 10
    s = 10 * (x - 1)
    l = len(str(n))
    s += (l * (l + 1)) // 2
    print(s)
