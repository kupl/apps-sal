#!/usr/bin/env python3
# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections
from decimal import Decimal # 10進数で考慮できる

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N, M = LI()

def primes(n): #試し割り法で各素因数とその指数を求める
    cnt=collections.defaultdict(int)
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            while n%i==0:
                cnt[i]+=1
                n//=i
    if n!=1:
        cnt[n]+=1
    return cnt


"""
O(N ** 0.5)で計算できる約数列挙

N = 20
make_divisors(20) = [1,2,4,5,10,20]
"""


def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

divs = make_divisors(M)

ans = -1
for i, divisior in enumerate(divs):
    if divisior > M // N:
        break
    else:
        ans = divisior

print(ans)

