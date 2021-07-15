H, W = map(int, input().split())

A = []
B = []
abs_diff = [[0]*(W+1) for h in range(H+1)]

for h in range(H):
  A.append(list(map(int, input().split())))
  
for h in range(H):
  B.append(list(map(int, input().split())))

max_diff = 0
for h in range(H):
  for w in range(W):
    d = abs(A[h][w] - B[h][w])
    max_diff = max(max_diff, d)
    abs_diff[h+1][w+1] = d

base = max_diff*(H + W)
dp = [[0 for w in range(W+1)] for h in range(H+1)]
dp[0][1] = dp[1][0] = 1 << base
for h in range(1, H+1):
  for w in range(1, W+1):
    dp[h][w] = (
      (dp[h-1][w] << abs_diff[h][w]) | (dp[h-1][w] >> abs_diff[h][w]) 
      | (dp[h][w-1] << abs_diff[h][w]) | (dp[h][w-1] >> abs_diff[h][w]))


positive = bin(dp[H][W] >> base)
print(positive[::-1].find('1'))
