n,a,b = map(int,input().split())
#sousuu = (2**n -1)%(10**9+7)

def cmb(n, r, mod):
    inv = [0,1]
    for i in range(2, r + 1):
        inv.append((-inv[mod % i] * (mod // i)) % mod)
    cmd = 1
    for i in range(1,min(r,n-r)+1):
        cmd = (cmd*(n-i+1)*inv[i])%mod
    return cmd

exceptA = cmb(n,a,10**9+7)
exceptB = cmb(n,b,10**9+7)

#print((sousuu-exceptA-exceptB)%(10**9+7))

#繰り返し2乗法
def modPow(a,n,mod):
    if n==0:
        return 1
    if n==1:
        return a%mod
    if n % 2 == 1:
        return (a*modPow(a,n-1,mod)) % mod
    t = modPow(a,n/2,mod)
    return (t*t)%mod

print((modPow(2,n,10**9+7)-1-exceptA-exceptB)%(10**9+7))
