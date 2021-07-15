H, N = map(int, input().split())
l = []
for i in range(N):
  l.append(list(map(int, input().split())))
  
dp = [0] * 20000
for i in range(1, 20001):
  dp[i] = min(dp[i-a]+b for a, b in l)
  if i == H:
    break
print(dp[H])
