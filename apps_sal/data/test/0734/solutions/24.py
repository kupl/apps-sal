n,m=list(map(int,input().split()))
l=list(map(int,input().split()))
l.sort()
c=max(l)
low=0
ans=0
for i in range(n-1):
    if l[i]>low:
        ans+=l[i]-1
        low+=1
    else:
        ans+=l[i]-1
if low==c:
    ans+=low-1
else:
    ans+=low
print(ans)
        
    

