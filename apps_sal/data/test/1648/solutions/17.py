
def pre_combi1(n, p):
    fact = [1]*(n+1)  # fact[n] = (n! mod p)
    factinv = [1]*(n+1)  # factinv[n] = ((n!)^(-1) mod p)
    inv = [0]*(n+1)  # factinv 計算用
    inv[1] = 1
    # 前処理
    for i in range(2, n + 1):
        fact[i]= fact[i-1] * i % p
        inv[i]= -inv[p % i] * (p // i) % p
        factinv[i]= factinv[i-1] * inv[i] % p
    return fact, factinv

def combi1(n, r, p, fact, factinv):
    """
    k<n<10**7でpが素数のときのnCr % pを求める
    """
    # 本処理
    if r < 0 or n < r:
        return 0
    r = min(r, n-r)
    return fact[n] * factinv[r] * factinv[n-r] % p

n,k=list(map(int,input().split()))
f,inv=pre_combi1(2005,10**9+7)
for i in range(1,k+1):
  print((combi1(n-k+1,i,10**9+7,f,inv)*combi1(k-1,i-1,10**9+7,f,inv)%(10**9+7)))


