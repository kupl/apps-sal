a,b,c=map(int,input().split())
m=min(a,b,c)
ans=m + int((a-m)/3)+int((b-m)/3)+int((c-m)/3)
if(m>0):
    m-=1
    ans=max(ans,m + int((a-m)/3)+int((b-m)/3)+int((c-m)/3))

print (ans)
