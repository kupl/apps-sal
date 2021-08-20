import math
import re
import itertools as it


def prime(n):
    return len([i for i in range(2, int(math.sqrt(n) + 1)) if n % i == 0]) == 0


def gcd(a, b):
    return gcd(b, a % b) if b else a


def fact(x):
    return x * fact(x - 1) if x else 1


def bino(n, k):
    return fact(n) / fact(k) / fact(n - k)


def fib11(n):
    return 1 if n < 2 else fib11(n - 1) + fib11(n - 2)


def fib01(n):
    return 0 if n == 0 else 1 if n == 1 else fib01(n - 1) + fib01(n - 2)


def sumofd(x):
    return x if x < 10 else sumofd(x // 10) + x % 10


(a, b, c) = map(int, input().split())
m = int(input())
d = []
for i in range(m):
    s = input().split()
    d.append([int(s[0]), 1 if s[1] == 'USB' else 0])
d.sort()
i = 0
p = 0
nn = 0
while i < len(d) and (a or b or c):
    f1 = f2 = False
    if a and d[i][1]:
        a -= 1
        p += d[i][0]
        f1 = True
        nn += 1
    if b and d[i][1] == 0:
        b -= 1
        p += d[i][0]
        f2 = True
        nn += 1
    if not f1 and (not f2):
        if c:
            c -= 1
            p += d[i][0]
            nn += 1
    i += 1
print(nn, p)
