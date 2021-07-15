mod = 998244353
n = int(input())
l = [tuple(map(int, input().split())) for _ in range(n)] + [(10**10, 0)]
l.sort()
st = [n]
nex = [n]*n
for i in range(n-1,-1,-1):
  x,d = l[i]
  v = x + d
  while l[st[-1]][0] < v: st.pop()
  nex[i] = st[-1]
  st.append(i)
dp = [0]*(n+1)
dp[n] = 1
for i in range(n-1,-1,-1):
  dp[i] = (dp[i+1] + dp[nex[i]]) % mod
print(dp[0])
