n,m = list(map(int,input().split()))
mod = 10**9+7 #出力の制限
import math

def perm(n, r):
    ''' nPr % mod '''
    if r > n:
        return 0
    return g1[n] * g2[n-r] % mod

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

N = 5 * 10**5
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

ans = 0
for k in range(n+1):
    a = cmb(n,k,mod)
    p1 = perm(m,k)
    p2 = perm(m-k, n-k)
    ans += (a * (-1)**k * p1 * p2**2)

print(ans%mod)
