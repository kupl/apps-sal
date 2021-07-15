n,m=list(map(int,input().split()))   
arr=list(map(int,input().split()))   
marr=list(map(int,input().split()))  
f=[0]*(m+1)
cnt,i=0,0
valid=sum(marr)   #m
while(i<n):
    f[arr[i]]+=1
    if f[arr[i]]<=marr[arr[i]-1]:
        cnt+=1
    if cnt==valid:
        break
    i+=1
if i==n:
    print(-1)
else:
    ans=(i+1)-valid
    s,e=0,i
    while(e<n):
        while(f[arr[s]]>marr[arr[s]-1]):
            f[arr[s]]-=1
            s+=1
        ans=min((e-s+1)-valid,ans)
        e+=1
        if e<n:
            f[arr[e]]+=1
    print(ans)
