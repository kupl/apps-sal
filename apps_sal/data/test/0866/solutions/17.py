import math

X,Y= list(map(int, input().split()))

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**6
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


if((X+Y) % 3 != 0):
    print(0)
    return

s = (-X + 2 * Y) // 3
t = (-Y + 2 * X) // 3


#print(s,t)

ans = cmb(s+t, s, 10**9+7)

print(ans)
