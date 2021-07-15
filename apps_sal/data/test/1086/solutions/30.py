import sys
input = sys.stdin.readline
h,w = map(int,input().split())
a = []
for i in range(h):
  s = list(map(int,input().split()))
  a.append(s)
  
b = []
for i in range(h):
  s = list(map(int,input().split()))
  b.append(s)
  
dp = [[0]*w for i in range(h)]
t = 80*(h+w)
dp[0][0] = 2**(t+abs(a[0][0]-b[0][0]))

for i in range(h):
  for j in range(w):
    r = abs(a[i][j]-b[i][j])
    if j > 0:
      dp[i][j] |= (dp[i][j-1]<<r | dp[i][j-1]>>r)
    if i > 0:
      dp[i][j] |= (dp[i-1][j]<<r | dp[i-1][j]>>r)
      
a = dp[h-1][w-1]>>t
m = a&(-a)
print(m.bit_length()-1)
