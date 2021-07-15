n,k = map(int,input().split())
mod = 10**9+7
ans = 0
m = {}
for i in range(k,0,-1):
  chk = pow(k//i,n,mod)
  t = k//i
  if t > 1:
    for j in range(2,t+1):
      chk -= m[i*j]
  m[i] = chk%mod
  ans += chk*i%mod
  ans %= mod
print(ans)
