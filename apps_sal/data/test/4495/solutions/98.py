a,b,x=map(int,input().split())
bb=b//x
aa=a//x
ans=bb-aa
if a%x==0:
    ans+=1
print(ans)
