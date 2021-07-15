H,W,N,*A = map(int,open(0).read().split())
B = []

for n in range(N):
  B+=A[n]*[n+1]

for h in range(H):
  print(*B[h*W:h*W+W][::1-h%2*2])
