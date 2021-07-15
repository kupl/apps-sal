n, c = map(int, input().split())
XV = [list(map(int, input().split())) for _ in range(n)]
X, V = zip(*XV)
dp_I_r = [0]*n
dp_U_r = [0]*n
dp_I_l = [0]*n
dp_U_l = [0]*n
dp_I_r[0] = V[0] - X[0]
dp_U_r[0] = V[0] - 2*X[0]
dp_I_l[n-1] = V[n-1] - (c - X[n-1])
dp_U_l[n-1] = V[n-1] - 2*(c - X[n-1])
for i in range(n-1):
  dp_I_r[i+1] = dp_I_r[i] + V[i+1] - (X[i+1] - X[i])
  dp_U_r[i+1] = dp_U_r[i] + V[i+1] - 2*(X[i+1] - X[i])
  dp_I_l[n-2-i] = dp_I_l[n-1-i] + V[n-2-i] - (X[n-1-i] - X[n-2-i])
  dp_U_l[n-2-i] = dp_U_l[n-1-i] + V[n-2-i] - 2*(X[n-1-i] - X[n-2-i])
for i in range(n-1):
  dp_I_r[i+1] = max(dp_I_r[i], dp_I_r[i+1])
  dp_U_r[i+1] = max(dp_U_r[i], dp_U_r[i+1])
  dp_I_l[n-2-i] = max(dp_I_l[n-1-i], dp_I_l[n-2-i])
  dp_U_l[n-2-i] = max(dp_U_l[n-1-i], dp_U_l[n-2-i])
ans = 0
for i in range(n):
  ans = max(ans, dp_I_r[i])
  ans = max(ans, dp_I_l[i])
  if i < n-1:
    ans = max(ans, dp_U_r[i] + dp_I_l[i+1])
  if i > 0:
    ans = max(ans, dp_U_l[i] + dp_I_r[i-1])
print(ans)
