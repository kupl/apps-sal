from collections import *
from math import *
N = int(input())
A = list(map(int,input().split()))
C = Counter(A)
S = 0

for k,v in C.items():
  S+=comb(v,2)

for a in A:
  print(S-(comb(C[a],2)-comb(C[a]-1,2)))
