def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**4
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

n,m = list(map(int,input().split()))

X = [0] + sorted(list(map(int,input().split())))
Y = [0] + sorted(list(map(int,input().split())))
sum1 = 0
sum2 = 0
MOD = 10 ** 9 + 7
for i in range(1, n + 1):
    sum1 += ((i - 1)*X[i] - (n - i)*X[i]) % MOD
for i in range(1, m + 1):
    sum2 += ((i - 1)*Y[i] - (m - i)*Y[i])%MOD
print((sum1 * sum2 % MOD))

