import math
import bisect
import heapq
from collections import defaultdict


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)


def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n



def isprime(n):
    for d in range(2, int(math.sqrt(n))+1):
        if n % d == 0:
            return False
    return True


def argsort(ls):
    return sorted(list(range(len(ls))), key=ls.__getitem__)


def f(p=0):
    if p == 1:
        return list(map(int, input().split()))
    elif p == 2:
        return list(map(int, input().split()))
    elif p == 3:
        return list(input())
    else:
        return int(input())

n = f()
s = f(3)
res = []
i = 0
while(i<n-1):
    while(i<n-1 and s[i]==s[i+1]):
        i+=1
    if i==n-1:
        break
    if s[i]!=s[i+1]:
        res.append(s[i])
        res.append(s[i+1])
    else:
        res.append(s[i])
    i+=2

if len(res)%2==0:
    print(n-len(res))
    print(''.join(res))
else:
    print(n-len(res)+1)
    print(''.join(res[:-1]))

