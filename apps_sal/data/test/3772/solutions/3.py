a,b=list(map(int,input().split()))



def Solve(a,b):
    if(a==(a//b)*b):
        return a//b
    if(a>b):
        ans=0
        ans+=a//b
        a%=b
        if(a==1):
            ans+=b
            return ans
        else:
            ans+=Solve(b,a)
            return ans
    else:
        return Solve(b,a)

print(Solve(a,b))

