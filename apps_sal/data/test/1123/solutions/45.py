n,k = map(int,input().split())
mod = 10**9+7

l = [0]*(k+1)

for i in range(k,0,-1):
  m = k//i
  l[i] += pow(k//i,n,mod)
  for j in range(2,m+1):
    l[i] -= l[i*j]

ans = 0
for i in range(k+1):
  ans += i*l[i] % mod
  ans %= mod
print(ans)
