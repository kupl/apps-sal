H, N = map(int, input().split())
AB=[[int(ab) for ab in input().split()] for n in range(N)]
dp=[0]*(20001)
for h in range(1, H+1):
  dp[h]=min(dp[h-a] + b for (a, b) in AB)
print(dp[H])
