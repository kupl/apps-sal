N,K = map(int,input().split())
P = list(map(int,input().split()))
Q = sum(P[:K])
R = Q

for n in range(N-K):
  Q = Q-P[n]+P[n+K]
  R = max(Q,R)

print((R+K)/2)
