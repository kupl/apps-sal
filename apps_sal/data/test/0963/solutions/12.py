n, k = map(int, input().split())
mod = 998244353
lr = []
s = set()
for i in range(k):
  l,r = map(int, input().split())
  for j in range(l,r+1):
    s.add(j)
  lr.append([l,r])

dp = [0 for i in range(n+1)]
dp[1] = 1
tot = [0 for i in range(k)]

for i in range(1,n+1):
  for j in range(k):
    l,r = lr[j][0],lr[j][1]
    if i-l < 1:
      continue
    tot[j] += dp[i-l]
    if i-r > 1:
      tot[j] -= dp[i-r-1]
    dp[i] += tot[j]
    dp[i] %= mod
print (dp[n])
