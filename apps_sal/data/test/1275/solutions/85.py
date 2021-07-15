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

n,k=list(map(int,input().split()))
ans=0

def num(j):

    if 2>j: return 0
    if j>2*n: return 0
    if j<n+1:
        return j-1
    sa= 2*(j-n-1)
    return j-1-sa
# a=0
# for i in range(max(2,2+k),2*n+1):
#     a+= num(i)
# c=0
# for i in range(2,2*n-k+1):
#     c+= num(i)

for i in range(2,2*n-k+1):
    # print("kore",i+k,i,)2525 -425

    a= num(i+k)
    b = num(i)
    ans+= a*b
    # print(a,b)

print(ans)

