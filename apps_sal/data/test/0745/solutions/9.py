n, k = list(map(int, input().split()))
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 998244353
N = 200000
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

if k == 0:
    ans = 1
    for i in range(1, n+1):
        ans *= i
        ans %= mod
    print(ans)

elif k >= n:
    print(0)

else:
    ans = 0
    K = n-k
    for i in range(K+1):
        ans += (-1)**((K-i)%2) * cmb(K, i, mod) * pow(i, n, mod)
    ans %= mod
    ans *= cmb(n, n-k, mod)
    ans *= 2
    ans %= mod
    print(ans)

