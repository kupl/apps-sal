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
def cdiv(n, k): return n // k + (n % k != 0)
def ii(): return int(input())
def mi(): return list(map(int, input().split()))
def li(): return list(map(int, input().split()))
def lcm(a, b): return abs(a*b) // math.gcd(a, b)

n = ii()
d = ii()
e = ii()

r = n%d
while n >= 5*e:
    n = n - (5*e)
    r = min(r, n%d)
print(r)


