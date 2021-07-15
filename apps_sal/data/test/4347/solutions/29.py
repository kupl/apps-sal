n=int(input())
def fact(n):
    res=1
    for i in range(2,n+1):
        res*=i
    return res;

z=n//2
ans=fact(n);
p=fact(z-1);

ans*=p*p;
ans/= fact(z);
ans/=fact(z);
ans/=2;
print(int(ans))
