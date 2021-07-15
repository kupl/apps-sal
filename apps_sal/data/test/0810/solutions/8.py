import sys

inf = float("inf")
# sys.setrecursionlimit(10000000)

# abc='abcdefghijklmnopqrstuvwxyz'
# abd={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
mod, MOD = 1000000007, 998244353
# words = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'quarter',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',21:'twenty one',22:'twenty two',23:'twenty three',24:'twenty four',25:'twenty five',26:'twenty six',27:'twenty seven',28:'twenty eight',29:'twenty nine',30:'half'}
# vow=['a','e','i','o','u']
# dx,dy=[0,1,0,-1],[1,0,-1,0]

# import random
# from collections import deque, Counter, OrderedDict,defaultdict
# from heapq import nsmallest, nlargest, heapify,heappop ,heappush, heapreplace
# from math import ceil,floor,log,sqrt,factorial,pi,gcd
# from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right

def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def input(): return sys.stdin.readline().strip()

def is_beautiful(sum):
    if sum==0:
        return 0
    while sum:
        if sum%10!=a:
            if sum%10!=b:
                return 0
        sum//=10
    return 1

def nCr(n,r):
    return (fact[n]*invfact[r]*invfact[n-r])%mod


# precalculating fact and inverse fact array

fact = [0]*(1000005)
invfact = [0]*(1000005)
fact[0] = fact[1] = invfact[0] = invfact[1] = 1
for i in range(1,1000003):
    fact[i] = (fact[i-1]%mod * i%mod)%mod
invfact[1000000] = pow(fact[1000000],mod-2,mod)
for i in range(999999,0,-1):
    invfact[i] = (invfact[i+1]%mod * (i+1)%mod)%mod

a,b,n = get_ints()
if a==b:
    if is_beautiful(a*n):
        print(1)
    else:
        print(0)
ans = 0
for i in range(n+1):
    if is_beautiful(a*i + b*(n-i)):
        ans+=nCr(n,i)
ans %=mod
print(ans)
