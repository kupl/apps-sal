from numpy import *
N,C = map(int,input().split())
A = zeros((C,10**5),int32)

for n in range(N):
  s,t,c = map(int,input().split())
  A[c-1,s-1:t] = 1
print(max(sum(A,axis=0)))
