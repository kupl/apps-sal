import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return map(int, minp().split())


n = mint()
y = 0
x = 0
a = []
t = 0
mx = dict()
my = 10**9
for i in mints():
    for j in range(i):
        if t == 0:
            a.append((x, y, '/'))
            mx[y] = max(mx.get(y, -1), x)
            my = min(my, y)
            y -= 1
        else:
            y += 1
            a.append((x, y, '\\'))
            mx[y] = max(mx.get(y, -1), x)
            my = min(my, y)
        x += 1
    t ^= 1
i = 0
b = []
while (my + i) in mx:
    b.append([' '] * (mx[my + i] + 1))
    i += 1
for i in a:
    b[i[1] - my][i[0]] = i[2]
for i in b:
    print(*(i + [' '] * (x - len(i))), sep='')
