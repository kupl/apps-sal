import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

m,n,k = list(map(int,readline().split()))

def comb(n, r, mod):
    r = min(r, n-r)
    mol = 1
    deno = 1
    for i in range(1, r+1):
        mol = mol * (n-r+i) % mod
        deno = deno * i % mod
    ret = mol * pow(deno, mod-2, mod) % mod
    return ret

ans = m*n*(m+n)*(m*n-1)//3

ans = (ans * comb(m*n-2,k-2,mod))%mod
ans = ans*pow(2,mod-2,mod)%mod

print(ans)


