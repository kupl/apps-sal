def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7
size = 2*10**5
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range( 2, size + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

H, W, A, B = map(int,input().split())

ans = 0

for i in range(W-B):
    ans += cmb(H-A-1+(B+i), B+i, mod) * cmb(A-1+W-B-1-i, A-1, mod)
    ans %= mod

print(ans)
