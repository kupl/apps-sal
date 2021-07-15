import heapq
import math
from collections import *
from functools import reduce,cmp_to_key
import sys

input = sys.stdin.readline
M = mod = 10**9 + 7
def factors(n):return sorted(list(set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))))
def inv_mod(n):return pow(n, mod - 2, mod)

def li():return [int(i) for i in input().rstrip('\n').split(' ')]
def st():return input().rstrip('\n')
def val():return int(input())
def li2():return [i for i in input().rstrip('\n').split(' ')]

for _ in range(val()):
    p = st()
    h = st()
    ans = 'NO'
    for i in range(len(h) - len(p) + 1):
        if sorted(p) == sorted(h[i:i+len(p)]):
            ans = 'YES'
            break
    print(ans)
