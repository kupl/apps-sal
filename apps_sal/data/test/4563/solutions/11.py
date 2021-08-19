import numpy as np
import sys


def sinput():
    return sys.stdin.readline()


def iinput():
    return int(sinput())


def imap():
    return map(int, sinput().split())


def fmap():
    return map(float, sinput().split())


def iarr():
    return list(imap())


def farr():
    return list(fmap())


def sarr():
    return sinput().split()


n = int(input())
tv = av = 1
t = [0] * n
a = [0] * n
for i in range(n):
    (t[i], a[i]) = imap()
for i in range(n):
    tmp = max(tv // t[i] + (tv % t[i] != 0), av // a[i] + (av % a[i] != 0))
    tv = t[i] * tmp
    av = a[i] * tmp
print(tv + av)
