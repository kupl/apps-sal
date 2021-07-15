import sys
import numpy as np
input = sys.stdin.readline
n,C = map(int,input().split())
a = np.zeros((C,10**5),dtype="int")
for _ in range(n):
  s,t,c = map(int,input().split())
  a[c-1,s-1:t] = 1
print(max(np.sum(a,axis=0)))
