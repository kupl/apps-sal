a1,b1,a2,b2=map(int,input().split())

import sys
sys.setrecursionlimit(2000000000)

p = 10 ** 9 + 7
N = a2+b2+2  # N は必要分だけ用意する
R = max(a2+1,b2+1)
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
  fact.append((fact[-1] * i) % p)
  
for i in range(2, R + 1):
  inv.append((-inv[p % i] * (p // i)) % p)
  factinv.append((factinv[-1] * inv[-1]) % p)

def comb(n, r, p):
  if (r < 0) or (n < r):
    return 0
  r = min(r, n - r)
  return fact[n] * factinv[r] * factinv[n-r] % p

score=comb(a2+b2+2,a2+1,p)-comb(a2+b1+1,a2+1,p)-comb(a1+b2+1,a1,p)+comb(a1+b1,a1,p)
print(score%(10**9+7))
