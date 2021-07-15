from copy import copy
from collections import Counter
from scipy.special import comb

n = int(input())
A = list(map(int,input().split()))

C = Counter(A)
S = 0
for i in range(1,n+1):
  S += comb(C[i],2,exact=True)

for k in range(n):
  p = A[k]
  ans = S - comb(C[p],2,exact=True) + comb(C[p]-1,2,exact=True)
  print(ans)
