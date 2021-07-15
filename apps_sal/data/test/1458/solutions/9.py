from bisect import bisect_right as br
from bisect import bisect_left as bl
from collections import *
from itertools import *
import functools
import sys
from math import *
import random
import re
MAX = sys.maxsize
MAXN = 10**5+10
MOD = 10**9+7
def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def mhd(a,b,x,y):
    return abs(a-x)+abs(b-y)

def numIN(x = " "):
    return(list(map(int,sys.stdin.readline().strip().split(x))))

def charIN(x= ' '):
    return(sys.stdin.readline().strip().split(x))

def arrIN():
    return list(numIN())

def dis(x,y):
    a = y[0]-x[0]
    b = x[1]-y[1]
    return (a*a+b*b)**0.5

def lgcd(a):
    g = a[0]
    for i in range(1,len(a)):
        g = math.gcd(g,a[i])
    return g

def ms(a):
    msf = -MAX
    meh = 0

    for i in range(len(a)):
        meh+=a[i]
        if msf<meh:
            msf = meh
        if meh<0:
            meh = 0
    return msf


def res(ans,t):
    print('Case #{}: {}'.format(t,ans))

n = int(input())
s = input()
for i in range(1,n):
    if s[i]<s[i-1]:
        print('YES')
        print(i,i+1)
        return

print('NO')

