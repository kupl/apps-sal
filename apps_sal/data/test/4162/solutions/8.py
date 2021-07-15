import sys
input = sys.stdin.readline # for speed up
#sys.setrecursionlimit(10**9)

n=int(input())
a=list(map(int,input().split()))

import math
r=0
for ii in range(1,n):
  r=(r*a[ii])//math.gcd(r,a[ii])

def func(x):
  y=0
  for aa in a:
    y+=x%aa
  return y

print((func(r-1)))

