import sys
input = sys.stdin.readline
h,w = list(map(int,input().split()))
la = [list(map(int,input().split())) for i in range(h)]
for i in range(h):
    l = list(map(int,input().split()))
    for j,num in enumerate(l):
        la[i][j] = abs(la[i][j]-num)
dp = [[0 for i in range(w)] for j in range(h)]
k = (h+w)*80+2
dp[0][0] = 1 << (k+la[0][0]) | 1 << (k-la[0][0])

for i in range(h):
    for j in range(w):
        if i:
            dp[i][j] |= (dp[i-1][j] << la[i][j]) | dp[i-1][j] >> la[i][j]
        if j:
            dp[i][j] |= (dp[i][j-1] << la[i][j]) | dp[i][j-1] >> la[i][j]
        
s = bin(dp[-1][-1])[2:]
l = len(s)-1
ans = float('inf')
for i in range(l,-1,-1):
  if s[i]=='1':
    m = abs(l-i-k)
    if m<ans:
      ans = m
print(ans)

