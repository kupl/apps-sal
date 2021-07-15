a,b=map(int,input().split())
ans=0
out=1
while out < b:
    out-=1
    out+=a
    ans+=1
print(ans)
