a,b=list(map(int,input().split()))

ans=a
while(a>=b):

    ans+=a//b
    a=a//b+a%b


print(ans)

