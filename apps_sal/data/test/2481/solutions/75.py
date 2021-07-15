H, W = map(int, input().split())
C = []
for i in range(10):
  c = list(map(int, input().split()))
  C.append(c)
A = []
for i in range(H):
  a = list(map(int, input().split()))
  A.append(a)
  
for k in range(10):
  for i in range(10):
    for j in range(10):
      if C[i][k]+C[k][j] < C[i][j]:
        C[i][j] = C[i][k] + C[k][j]
        
ans = 0
for i in range(H):
  l = A[i]
  for j in range(W):
    n = l[j]
    if (n==0) or (n>1):
      ans += C[n][1]
print(ans)
