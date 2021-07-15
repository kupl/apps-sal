import sys
input = sys.stdin.readline
from math import gcd
from operator import mul
from functools import reduce
 
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
 
    arr.sort()
    best = - (10**99)
    
    tmp = arr[-5:]
    tmp = reduce(lambda x, y: x * y, tmp, 1)
    best = max(best, tmp)
    
    tmp = arr[:2] + arr[-3:]
    tmp = reduce(lambda x, y: x * y, tmp, 1)
    best = max(best, tmp)
    
    tmp = arr[:4] + arr[-1:]
    tmp = reduce(lambda x, y: x * y, tmp, 1)
    best = max(best, tmp)
    
    print(best)
