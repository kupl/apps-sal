H,W,D = map(int,input().split())
P = [None]*(H*W+1)

for h in range(H):
  A = list(map(int,input().split()))
  for w in range(W):
    P[A[w]] = [h,w]

B = [0]*(H*W+1)

for n in range(D+1,H*W+1):
  B[n] = B[n-D]+abs(P[n][0]-P[n-D][0])+abs(P[n][1]-P[n-D][1])

Q = int(input())
ans = 0
for q in range(Q):
  L,R = map(int,input().split())
  print(B[R]-B[L])
