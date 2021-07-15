MOD = 1_000_000_007
def calc_combi(n,k):
    frac=1
    denomi=1
    for i in range(n-k+1,n+1):
        frac=frac*i%MOD
    for i in range(1,k+1):
        denomi=denomi*i%MOD
    return frac*pow(denomi,MOD-2,MOD)

n, a, b = map(int,input().rstrip().split())
nca = calc_combi(n,a)
ncb = calc_combi(n,b)
print((pow(2,n,MOD)-1-nca-ncb)%MOD)
