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
def prr(a, sep = ' '): print(sep.join(map(str, a)))

n = ii()
s = input()
t = input()
if (s.count('a') + t.count('a'))%2:
    print(-1);return()

ab = []
ba = []
for i in range(n):
    if s[i] == 'a' and t[i] == 'b':
        ab.append(i + 1)
    elif s[i] == 'b' and t[i] == 'a':
        ba.append(i + 1)

r = []
while len(ab) >= 2:
    v = ab.pop()
    u = ab.pop()
    r.append(f'{u} {v}')
while len(ba) >= 2:
    v = ba.pop()
    u = ba.pop()
    r.append(f'{u} {v}')

if len(ab) != len(ba):
    print(-1);return()
elif len(ab) > 0:
    u = ab[0]
    v = ba[0]
    r.append(f'{u} {u}')
    r.append(f'{u} {v}')

print(len(r))
for i in r:
    print(i)
