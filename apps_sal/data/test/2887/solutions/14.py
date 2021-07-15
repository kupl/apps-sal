n=int(input())
v=list(map(int,input().split()))
t=list(map(int,input().split()))
for i in range(n):
    ans=0
    for j in range(0,i+1):
        if t[i]<=v[j]:
            ans+=t[i]
            v[j]=v[j]-t[i]
        else:
            ans+=v[j]
            v[j]=0
    print(ans,end=' ')
    

