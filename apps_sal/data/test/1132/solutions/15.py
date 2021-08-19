import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


(n, m) = mints()
e = [[] for i in range(n + 1)]


def isstar():
    c = None
    for i in range(1, n + 1):
        if len(e[i]) > 1:
            if c != None:
                return False
            c = i
    if c == None:
        return False
    return len(e[c]) == n - 1


def isbus():
    c = None
    for i in range(1, n + 1):
        if len(e[i]) == 1:
            c = i
    if c == None:
        return False
    cnt = 2
    p = c
    c = e[c][0]
    while len(e[c]) == 2:
        if e[c][0] == p:
            p = c
            c = e[c][1]
        else:
            p = c
            c = e[c][0]
    return len(e[c]) == 1


def isring():
    p = 1
    if len(e[1]) != 2:
        return False
    c = e[1][0]
    while len(e[c]) == 2 and c != 1:
        if e[c][0] == p:
            p = c
            c = e[c][1]
        else:
            p = c
            c = e[c][0]
    return c == 1


for i in range(m):
    (a, b) = mints()
    e[a].append(b)
    e[b].append(a)
if isstar():
    print('star topology')
elif isbus():
    print('bus topology')
elif isring():
    print('ring topology')
else:
    print('unknown topology')
