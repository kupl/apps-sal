n,m,k=list(map(int,input().split()))
U = 2*10**5
MOD = 10**9+7
 
fact = [1]*(U+1)
fact_inv = [1]*(U+1)
 
for i in range(1,U+1):
  fact[i] = (fact[i-1]*i)%MOD
fact_inv[U] = pow(fact[U],MOD-2,MOD)
 
for i in range(U,0,-1):
	fact_inv[i-1] = (fact_inv[i]*i)%MOD
 
def comb(n,k):
  if k < 0 or k > n:
    return 0
  x = fact[n]
  x *= fact_inv[k]
  x %= MOD
  x *= fact_inv[n-k]
  x %= MOD
  return x

ans=0
for i in range(n):
    for j in range(m):
        if i!=0 and j!=0:
            ans+=2*(n-i)*(m-j)*(i+j)
        else:
            ans+=(n-i)*(m-j)*(i+j)
        ans%=MOD

print((ans*comb(n*m-2,k-2)%MOD))


