import math
import sys
import collections


# imgur.com/Pkt7iIf.png

def getdict(n):
    d = {}
    if type(n) is list:
        for i in n:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    else:
        for i in range(n):
            t = ii()
            if t in d:
                d[t] += 1
            else:
                d[t] = 1
    return d


def sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = prime[1] = False
    r = [p for p in range(n + 1) if prime[p]]
    return r


def cdiv(n, k): return n // k + (n % k != 0)
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))
def lcm(a, b): return abs(a * b) // math.gcd(a, b)
def prr(a, sep=' '): print(sep.join(map(str, a)))


n = ii()
s = input()
l = r = tl = tr = 0
for i in s[:n // 2]:
    if i == '?':
        tl += 1
    else:
        l += int(i)
for i in s[n // 2:]:
    if i == '?':
        tr += 1
    else:
        r += int(i)

if tl == tr == 0:
    print('Bicarp') if l == r else print('Monocarp')
    return

if l + cdiv(tl, 2) * 9 - r > cdiv(tr, 2) * 9 or r + cdiv(tr, 2) * 9 - l > cdiv(tl, 2) * 9:
    print('Monocarp')
else:
    print('Bicarp')
