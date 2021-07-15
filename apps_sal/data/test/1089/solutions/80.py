U = 2*10**5
MOD = 10**9+7
 
fact = [1]*(U+1)
fact_inv = [1]*(U+1)
 
for i in range(1,U+1):
    fact[i] = (fact[i-1]*i)%MOD
fact_inv[U] = pow(fact[U], MOD-2, MOD)
 
for i in range(U,0,-1):
    fact_inv[i-1] = (fact_inv[i]*i)%MOD

def comb(n, k):
    if k < 0 or k > n:
        return 0
    z = fact[n]
    z *= fact_inv[k]
    z *= fact_inv[n-k]
    z %= MOD
    return z

n, m, k = map(int, input().split())
ans = ((n-1)*n*(n+1)//6*m**2 + (m-1)*m*(m+1)//6*n**2) * comb(n*m-2, k-2)
print(ans%MOD)
