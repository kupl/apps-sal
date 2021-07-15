def f(i):
  if i == W-1:
    for j in range(W-2):
      if s[j] == s[j+1] == 1:
        return
    nonlocal x
    for j in range(W):
      if j == 0:
        if s[0] == 1:
          x[0][1] += 1
        else:
          x[0][0] += 1
      elif j == W - 1:
        if s[W-2] == 1:
          x[W-1][W-2] += 1
        else:
          x[W-1][W-1] += 1
      else:
        if s[j-1] == 1:
          x[j][j-1] += 1
        elif s[j] == 1:
          x[j][j+1] += 1
        else:
          x[j][j] += 1 
    return
  s[i] = 1
  f(i + 1)
  s[i] = 0
  f(i + 1)

H,W,K=map(int, input().split())
MOD = pow(10, 9) + 7
s = [0] * (W - 1)
x = [[0] * W for _ in range(W)]
if not W == 1:
  f(0)
else:
  print(1)
  return
dp = [[0] * W for _ in range(H+1)]
dp[0][0] = 1
for i in range(1,H+1):
  for j in range(W):
    for l in range(W):
      dp[i][j]+=dp[i-1][l]*x[l][j]
      dp[i][j]%=MOD
print(dp[H][K-1])
