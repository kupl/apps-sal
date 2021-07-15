ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
ips = lambda:input().split()
import collections
import math
import itertools
import heapq as hq
import sys
ceil = math.ceil
gcd = math.gcd
RL = sys.stdin.readline
INF=10**15
def ceilab(a,b):
    return (a+b-1)//b

n=ni()
l = 0
r=n+1
while r-l>1:
    x = (r+l)//2
    if x*(x+1)//2 >n+1:
        r=x
    else:
        l=x
print(n+1-l)

