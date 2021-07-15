N = int(input())
lis = [input() for _ in range(4)]
if N==2:
  print((1))
  return
dp1 = [0]*(N+1)
dp1[0] = 1
MOD = 10**9+7
for i in range(1,N+1):
  for j in range(i-1):
    dp1[i] += dp1[j]
    dp1[i] %= MOD
# dp2 = [[0]*2 for _ in range(N+1)]
# dp2[0][1] = 1
# for i in range(1,N+1):
#   for j in range(i):
#     dp2[i][0] += dp2[j][1]
#     dp2[i][0] %= MOD
#     dp2[i][1] += dp2[j][0]
#     dp2[i][1] %= MOD
if lis[1]=='A':
  if lis[0]=='A':
    ans = 1
  elif lis[2]=='A':
    ans = dp1[-1]
  else:
    ans = pow(2,N-3,MOD)
else:
  if lis[3]=='B':
    ans = 1
  elif lis[2]=='B':
    ans = dp1[-1]
  else:
    ans = pow(2,N-3,MOD)
print(ans)


