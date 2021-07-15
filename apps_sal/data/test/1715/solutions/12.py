from bisect import *
A,B,Q = map(int,input().split())
inf = float("inf")
S = [-inf]+[int(input()) for a in range(A)]+[inf]
T = [-inf]+[int(input()) for b in range(B)]+[inf]
X = [int(input()) for q in range(Q)]

for x in X:
  si = bisect(S,x)
  ti = bisect(T,x)
  d1 = x-S[si-1]
  d2 = S[si]-x
  d3 = x-T[ti-1]
  d4 = T[ti]-x
  print(min(2*d1+d4,d1+d4*2,2*d2+d3,d2+d3*2,max(d1,d3),max(d2,d4)))
