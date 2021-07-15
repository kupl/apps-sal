n,d=list(map(int,input().split()))
a=list(map(int,input().split()))
s=0
m=0
ans=0 
flag=True
n=len(a)
for i in range(n):
    if a[i]==0:
        if s<0:
            s=d
            m=d
            ans+=1
        else:
            m=min(m,s)
    elif a[i]<0:
        s=s+a[i] 
    else:
        if(s+a[i]>d):
            if(s+a[i]-d)>m:
                flag=False
                break 
            else:
                m-=(s+a[i]-d)
                s=d 
        else:
            s=s+a[i] 
if flag:
    print(ans)
else:
    print(-1)
