from fractions import *


def f():
    return map(int, input().split())


m = int(input())


def g(u, v):
    (h, a) = u
    (x, y) = v
    s = 0
    while h != a:
        h = (h * x + y) % m
        s += 1
        if s > m:
            break
    h = (a * x + y) % m
    d = 1
    while h != a:
        h = (h * x + y) % m
        d += 1
        if d > m:
            break
    return (s, d)


((u, x), (v, y)) = (g(f(), f()), g(f(), f()))
if u > m or v > m:
    q = -1
elif u == v:
    q = u
elif x > m:
    q = -1 if u < v or (v - u) % y else u
elif y > m:
    q = -1 if v < u or (v - u) % x else v
elif (v - u) % gcd(x, y):
    q = -1
else:
    while u != v:
        if u < v:
            u += x
        else:
            v += y
    q = u
print(q)
