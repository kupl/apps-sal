import sys
try:
    import os
    f = open('input.txt', 'r')
    sys.stdin = f
except FileNotFoundError:
    None
from math import sqrt, ceil, floor
from collections import deque, Counter, defaultdict
# defaultdict(int)
input=lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(11451419)
from decimal import ROUND_HALF_UP,Decimal  #変換後の末尾桁を0や0.01で指定
  #Decimal((str(0.5)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
from functools import lru_cache
from bisect import bisect_left as bileft, bisect_right as biright, insort
from itertools import combinations as com, permutations as per
from fractions import Fraction as frac  #frac(a,b)で正確なa/b
# @lru_cache(maxsize=10**10)
#######ここまでテンプレ#######
#ソート、"a"+"b"、再帰ならPython3の方がいい
#######ここから天ぷら########

def f(n):
    return n*(n+1)//2

a,b,c=list(map(int,input().split()))
mod=998244353
print((((f(a)%mod)*(f(b)%mod)*(f(c)%mod))%mod))

