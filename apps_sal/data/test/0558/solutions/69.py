N, M, K = list(map(int, input().split()))
ans = 0
mod = 998244353

fact = [0] * 200001
invfact = [0] * 200001
fact[0] = 1
invfact[0] = 1

for i in range(1, 200001):
    fact[i] = fact[i-1] * i % mod
    
invfact[-1] = pow(fact[-1], mod-2, mod)

for i in reversed(list(range(1, 200000))):
    invfact[i] = invfact[i+1] * (i+1) % mod

for k in range(K+1):
    ans += invfact[N-1-k] * invfact[k] *pow((M-1),N-1-k, mod) % mod
    ans %= mod

ans = ans * M * fact[N-1] % mod

print(ans)



