def cmb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % mod
mod = 10**9 + 7

fact = [1, 1]
factinv = [1, 1]
inv = [0,1]

n, k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
if k == 1:
    print(0)
    return

for i in range(2,n+1):
    fact.append((fact[-1] * i) % mod)
    inv.append((inv[mod % i] * (mod - (mod // i))) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)

saidai = 0
saisyo = 0

for i in range(n-k+1):
    saisyo += (a[i]*cmb(n-i-1,k-1,mod))%mod
    saisyo %= mod
for i in range(k-1,n):
    saidai += (a[i]*cmb(i,k-1,mod))%mod
    saidai %= mod
print((saidai-saisyo)%mod)
