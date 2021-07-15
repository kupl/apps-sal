mod=1000000007
def fastexp(base,exp):
    if(exp==0):
        return 1;
    if(exp==1):
        return base%mod;
    t=fastexp(base,exp//2);
    if(exp%2==0):
        return (t%mod*t%mod)%mod;
    else:
        return (t%mod*t%mod*base%mod)%mod;
x,k=list(map(int,input().split()))
if(x==0):
    print((0));
else:
    t=fastexp(2,k)%mod;
    before=((2*t)%mod*x%mod)%mod-(t+mod-1)%mod
    while(before<0):
        before+=mod;
    before=before%mod;
    print(before)

