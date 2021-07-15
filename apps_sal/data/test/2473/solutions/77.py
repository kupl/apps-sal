N,K = map(int,input().split())
A = sorted([list(map(int,input().split()))for n in range(N)])
ans = float("inf")

for i in range(N-K+1):
  for j in range(i+K-1,N):
    P = A[j][0]-A[i][0]
    C = sorted([a[1] for a in A[i:j+1]])
    for k in range(j-i-K+2):
      Q = C[k+K-1]-C[k]
      ans = min(ans,P*Q)

print(ans)
