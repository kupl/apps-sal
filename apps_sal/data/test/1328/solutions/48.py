N,Ma,Mb=map(int, input().split())
A = []
B = []
C = []
for i in range(N):
  a,b,c=map(int, input().split())
  A.append(a)
  B.append(b)
  C.append(c)
sa = sum(A)
sb = sum(B)

dp = [[[10000]*(sb+1) for _ in range(sa+1)] for _ in range(N+1)]
dp[0][0][0] = 0

ta = 0
tb = 0
for i in range(N):
  a = A[i]
  b = B[i]
  for j in range(sa):
    for k in range(sb):
      if j - a >= 0 and k - b >= 0:
        dp[i+1][j][k] = min(dp[i][j-a][k-b]+C[i], dp[i][j][k])
      else:
        dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])

ans = 10000
for i in range(1, sa+1):
  for j in range(1, sb+1):
    if Ma * j == Mb * i:
      ans = min(ans, dp[N][i][j])
if ans == 10000:
  ans = -1
print(ans)
