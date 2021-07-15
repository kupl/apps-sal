a, b = map(int, input().split())
m=max(a,b)
mm=min(a,b)
ans=0
while(mm!=1):
    ans=ans+m//mm
    i=m%mm
    if(i>mm):
        m=i
    else:
        m=mm
        mm=i
ans=ans+m
print(round(ans))
