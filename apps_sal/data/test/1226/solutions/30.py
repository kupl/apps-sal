def calc_comb(n,r):
    numerator=1
    for i in range(n-r+1,n+1):
        numerator=(numerator*i)%mod
    denominator=1
    for i in range(1,r+1):
        denominator=(denominator*i)%mod
    return (numerator*pow(denominator,mod-2,mod))%mod
n,a,b=list(map(int,input().split()))
mod=1000000007
print(((pow(2,n,mod)-1-calc_comb(n,a)-calc_comb(n,b)+mod)%mod))


