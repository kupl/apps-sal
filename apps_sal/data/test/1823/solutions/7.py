import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


n, k = mints()
a = list(mints())
i = 0
c = [0] * (k + 1)
while i < n:
    j = i
    while j < n and a[j] == a[i]:
        j += 1
    if i - 1 >= 0:
        if j < n:
            if a[i - 1] != a[j]:
                c[a[i]] += 1
            else:
                c[a[i]] += 2
        else:
            c[a[i]] += 1
    elif j < n:
        c[a[i]] += 1
    i = j
z = 1
for i in range(k + 1):
    if c[z] < c[i]:
        z = i
print(z)
