from sys import stdin, stdout
from math import factorial
from math import log10
INF = float('inf')


def gcd(a, b):
    if not b:
        return a
    else:
        return gcd(b, a % b)


def f(a, b, u):
    if not b:
        return 0
    if not fact:
        return b // u
    mx = -INF
    for v in fact:
        if b - b % (u * v) > mx:
            mx = max(mx, b - b % (u * v))
            cur = v
    while not mx and fact:
        fact.pop()
    if mx:
        fact.pop(fact.index(cur))
        return (b - mx) // u + f(a, mx, u * cur)
    else:
        return f(a, b, u)


(a, b) = map(int, stdin.readline().split())
fact = []
q = gcd(a, b)
i = 2
k = a // q
while i * i <= a:
    while not k % i:
        fact.append(i)
        k //= i
    i += 1
if k != 1:
    fact.append(k)
stdout.write(str(f(a, b, q)))
