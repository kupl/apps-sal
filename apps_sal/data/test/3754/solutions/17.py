import numpy as np
import sys
from sys import stdin

def main():
  s=sum(d)
  ans=1
  for i in range(n):
    ans=ans*d[i]%m
  for i in range(n,2*n-2):
    ans=ans*(s-i)%m
  return ans

input = sys.stdin.readline
n=int(input())
d=list(map(int,input().split()))
m=998244353
print(main())
