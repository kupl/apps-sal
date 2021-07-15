from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush,heappop
import math
from collections import *
from functools import reduce,cmp_to_key
# import io, os
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
import sys
input = sys.stdin.readline

M = mod = 10**9 + 7
def factors(n):return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n):return pow(n, mod - 2, mod)

def li():return [int(i) for i in input().split()]
def st():return input()
def val():return int(input().rstrip('\n'))
def li2():return [i for i in input().rstrip('\n')]
def li3():return [int(i) for i in input().rstrip('\n')]

def giveab(a,b):
    l = []
    for i in range(1,a * b + 1,1):
        l.append(1 if ((i%a)%b) != ((i%b)%a) else 0)
    return l[:]

def giveforanum(r,s,l):
    temp = r//(a * b)
    up = temp*s
    r %= (a * b)
    
    return up + l[r]


for _ in range(val()):
    a,b,q = li()
    
    l1 = giveab(a,b)
    pref = [0]
    for i in l1:pref.append(pref[-1] + i)

    s = sum(l1)
    ans = []
    for i in range(q):
        l,r = li()
        ans.append(giveforanum(r,s,pref) - giveforanum(l-1,s,pref))
    print(*ans)
