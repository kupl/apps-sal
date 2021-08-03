import sys
from math import *
sys.setrecursionlimit(100000000)


def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def ppcm(a, b):
    if (a == 0) or (b == 0):
        return 0
    else:
        return (a * b) // pgcd(a, b)


t, w, b = map(int, input().split())
a = ppcm(w, b)
x = min(w, b)
y = t // a
v = x * y + min(x, t % a + 1) - 1

w = pgcd(v, t)
if v == 0:
    print("0/1")
else:
    print(v // w, end="")
    print("/", end="")
    print(t // w)
