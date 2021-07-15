from numpy import *
N,K = map(int,input().split())
P = list(map(int,input().split()))
Q = (N-K+1)*[0]
R = sum(P[0:K])
Q[0] = R

for n in range(1,N-K+1):
  R+=P[n-1+K]-P[n-1]
  Q[n] = R

S = argmax(Q)
print(0.5*(sum(P[S:S+K])+K))
