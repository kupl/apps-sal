from math import *

def r1(t):
    return t(input())

def r2(t):
    return [t(i) for i in input().split()]

for _ in range(r1(int)):
    n = r1(int)
    i = 2
    a = 1
    b = n - 1
    while i * i <= n:
        if n % i == 0:
            t = n // i
            a = max(a, t)
            b = min(b, n - t)
        i += 1
    print(a, b)

