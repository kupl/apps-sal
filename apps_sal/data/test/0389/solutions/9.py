# -*- coding: utf-8 -*-

def gcd(a, b):
    if a > b:
        a, b = b, a
    while True:
        t = b % a
        if t == 0:
            return a
        a, b = t, a
    return 1

a, b = map(int, input().split())
g = gcd(a, b)
m = a/g * b/g
n = 0
while m % 2 == 0:
    m /= 2
    n += 1
while m % 3 == 0:
    m /= 3
    n += 1
while m % 5 == 0:
    m /= 5
    n += 1
print(n if m == 1 else -1)
