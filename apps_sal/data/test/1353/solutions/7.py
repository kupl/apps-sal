n,m,a,b=map(int,input().split())
if m*a<=b:
    print(n*a)
else:
    ans=n//m*b
    if n%m!=0:
        if (n%m)*a<b:
            ans+=a*(n%m)
        else:
            ans+=b
    print(ans)
