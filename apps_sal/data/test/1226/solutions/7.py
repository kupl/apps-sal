n,a,b = map(int, input().split())
mod = 10**9+7

def cmb(n,r):
    a,b = 1,1
    for i in range(r):
        a = a * (n-i) % mod
        b = b * (i+1) % mod
    return a * pow(b, mod-2, mod) %mod

print((pow(2, n, mod) - cmb(n,a) - cmb(n,b) - 1)%mod)
