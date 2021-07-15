n=int(input())
t=list(map(int,input().split()))
v=list(map(int,input().split()))+[0]
for i in range(n-1,-1,-1):
    v[i]=min(v[i],v[i+1]+t[i])
ans=0
v0=0
for i in range(n):
    if v[i]<=v[i+1]:
        if v[i]-v0>t[i]:
            ans+=(2*v0+t[i])*t[i]/2
            v0=v0+t[i]
        else:
            ans+=t[i]*v[i]-(v[i]-v0)**2/2
            v0=v[i]
    else:
        if v[i]*2-v0-v[i+1]<t[i]:
            ans+=t[i]*v[i]-(v[i]-v0)**2/2-(v[i]-v[i+1])**2/2
            v0=v[i+1]
        elif v[i+1]-v0>t[i]:
            ans+=(2*v0+t[i])*t[i]/2
            v0=v0+t[i]
        else:
            d=abs(v0-v[i+1])
            ans+=max(v0,v[i+1])*t[i]-d**2/2+(t[i]-d)**2/4
            v0=v[i+1]
print(ans)
