from collections import *
from functools import reduce,cmp_to_key
import sys
input = sys.stdin.readline
M = mod = 998244353
def factors(n):return sorted(list(set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))))
def inv_mod(n):return pow(n, mod - 2, mod)
 
def li():return [int(i) for i in input().rstrip('\n').split(' ')]
def st():return input().rstrip('\n')
def val():return int(input())
 
n = val()
exp = 0
for pi in li():
    exp = (exp+1) * 100 * pow(pi,M-2,M) % M
 
print(exp)
#From SMMaster

