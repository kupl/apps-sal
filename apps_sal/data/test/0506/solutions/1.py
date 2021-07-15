a,b=map(int,input().split())
ans=0
a,b=max(a,b),min(a,b)
while b!=0:
    ans+=a//b
    a,b=b,a%b
print(ans)
