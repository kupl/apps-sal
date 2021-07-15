import sys
import math
import itertools
import collections


def sieve(n):
    if n < 2: return list()
    prime = [True for _ in range(n + 1)]
    p = 3
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 2
    r = [2]
    for p in range(3, n + 1, 2):
        if prime[p]:
            r.append(p)
    return r
def divs(n, start=1):
    r = []
    for i in range(start, int(math.sqrt(n) + 1)):
        if (n % i == 0):
            if (n / i == i):
                r.append(i)
            else:
                r.extend([i, n // i])
    return r
def cdiv(n, k): return n // k + (n % k != 0)
def ii(): return int(input())
def mi(): return list(map(int, input().split()))
def li(): return list(map(int, input().split()))
def lcm(a, b): return abs(a * b) // math.gcd(a, b)
def wr(arr): return ''.join(map(str, arr))
def revn(n): return str(n)[::-1]
def prime(n):
    if n == 2: return True
    if n % 2 == 0 or n <= 1: return False
    sqr = int(math.sqrt(n)) + 1
    for d in range(3, sqr, 2):
        if n % d == 0: return False
    return True
def convn(number, base):
    newnumber = 0
    while number > 0:
        newnumber += number % base
        number //= base
    return newnumber


t = ii()
for _ in range(t):
    n, m = mi()
    a = li()
    if n > m or n == 2:
        print(-1)
    else:
        ans = 2 * sum(a)
        mina = min(a)
        posmin = a.index(min(a))
        b = a.copy()
        b.sort()
        posmin1 = a.index(b[1])
        if posmin == posmin1:
            posmin1 = a.index(b[1], posmin + 1)
        ans += (mina + b[1]) * (m - n)
        print(ans)
        for i in range(n - 1):
            print(i + 1, i + 2)
        print(n, 1)
        for i in range(m - n):
            print(posmin + 1, posmin1 + 1)

