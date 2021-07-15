n,k=list(map(int, input().split()))


def cmb(n, r, p):
  if (r < 0) or (n < r):
    return 0
  r = min(r, n - r)
  return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
N = 2*(10 ** 5 ) # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p) 階乗のmod
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用 

for i in range(2, N + 1):
  fact.append((fact[-1] * i) % p)
  inv.append((-inv[p % i] * (p // i)) % p)
  factinv.append((factinv[-1] * inv[-1]) % p)

#0の数がmin(n-1,k)
MAX=min(n-1,k)

dp=[0]*(MAX+1)
dp[0]=1
ans=1
for i in range(1,MAX+1):
    ans+=cmb(n,i,p)*cmb(n-i+i-1,i,p)
    ans%=p
    #print(ans)

print(ans)

