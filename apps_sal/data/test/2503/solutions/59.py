from numpy import *
N,K = map(int,input().split())
M = zeros((3*K,3*K),int)
L = 2*K
O = 0

for n in range(N):
  x,y,c = input().split()
  x = int(x)%L
  y = int(y)%L
  t = c=="W"
  M[x,y]+=1-2*t
  O+=t

for n in range(2):
  M[L:] = M[:K]
  M = cumsum(M,axis=0)
  M[:L] = M[K:]-M[:L]
  M = M.T
  
M = M[:L,:L]
print(O+(M+roll(roll(M,K,axis=0),K,axis=1)).max())
