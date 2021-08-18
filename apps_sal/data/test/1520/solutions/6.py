from math import *
import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


n = mint()
a = [0] * 256
b = [0] * 256
for k in range(0, n):
    for i in range(ord('a'), ord('z') + 1):
        b[i] = min(a[i], 1)
    i = 0
    s = list(minp())
    l = len(s)
    q = 0
    while i < l:
        j = i + 1
        while j < l and s[j] == s[i]:
            j += 1
        z = ord(s[i])
        w = j - i
        if i == 0:
            q = w
            if j == l:
                w += (w + 1) * a[z]
            elif a[z] != 0:
                w += 1
        elif j == l:
            w += 1
            if s[0] == s[-1]:
                w += q
        b[z] = max(b[z], w)
        i = j
    a, b = b, a
print(max(a))
