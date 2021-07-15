a,b=map(int,input().split())
ans=0
a1=a
r=0
while a1!=0:
    ans+=a1
    a1=(a+r)//b
    r=a+r-a1*b
    a=a1
print(ans)
